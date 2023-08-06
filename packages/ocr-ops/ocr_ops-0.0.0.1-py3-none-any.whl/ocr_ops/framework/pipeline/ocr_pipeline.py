import os
from typing import Optional, Dict, Any, List, Union

import cv2
from algo_ops.ops.op import Op
from algo_ops.paraloop import paraloop
from algo_ops.pipeline.cv_pipeline import CVPipeline
from algo_ops.pipeline.pipeline import Pipeline
from natsort import natsorted

from ocr_ops.dependency import sys_util
from ocr_ops.framework.op.ocr_op import OCRMethod, OCROp


class OCRPipeline(Pipeline):
    """
    OCR Pipeline supports running various OCR methods on an image to generate text. It supports
    using a CVOps image pre-processing pipeline to prepare an image for OCR. It also supports a
    text post-processing pipeline to clean noisy OCR-ed text results to return a final robust
    callset of OCR-ed text from an image.
    """

    @staticmethod
    def get_image_files(images_dir: str) -> List[str]:
        """
        Get image paths for images in an images directory.

        param images_dir: The images directory

        return: Image file paths
        """
        files = natsorted(
            [os.path.join(images_dir, file) for file in os.listdir(images_dir)]
        )
        return files

    def __init__(
        self,
        img_pipeline: Optional[CVPipeline],
        ocr_method: OCRMethod,
        text_pipeline: Optional[Pipeline],
    ):
        """
        param img_pipeline: An optional CVOps pre-processing pipeline to run on image before OCR
        param ocr_method: The ocr method to use
        param text_pipeline: An optional TextOps pipeline to post-process OCR text
        """
        self.img_pipeline = img_pipeline
        self.ocr_op = OCROp(ocr_method=ocr_method)
        self.text_pipeline = text_pipeline

        # prepare operations
        ops: List[Op] = list()
        # image preprocessing steps
        if self.img_pipeline is not None:
            ops.append(self.img_pipeline)
        # actual OCR on image
        ops.append(self.ocr_op)
        # text cleaning post-processing
        if self.text_pipeline is not None:
            ops.append(self.text_pipeline)
        super().__init__(ops=ops)

    def run_on_img_file(self, file: str) -> Union[str, List[str]]:
        """
        Runs OCR pipeline on input image file.

        param file: Path to input image file

        return:
            output: Text OCR-ed from image
        """
        img = cv2.imread(filename=file)
        return self.exec(inp=img)

    def set_img_pipeline_params(self, func_name: str, params: Dict[str, Any]) -> None:
        """
        Fixes parameters of CVOPs processing pipeline.

        param func_name: The function name in CVOPs pipeline
        param params: Dict mapping function param -> value
        """
        if self.img_pipeline is None:
            raise ValueError("Cannot set parameters when img_pipeline=None.")
        self.img_pipeline.set_pipeline_params(func_name=func_name, params=params)

    def set_text_pipeline_params(self, func_name: str, params: Dict[str, Any]) -> None:
        """
        Fixes parameters of CVOPs processing pipeline.

        param func_name: The function name in CVOPs pipeline
        param params: Dict mapping function param -> value
        """
        if self.text_pipeline is None:
            raise ValueError("Cannot set parameters when text_pipeline=None.")
        self.text_pipeline.set_pipeline_params(func_name=func_name, params=params)

    def save(self, out_path: str = "") -> None:
        """
        Saves image pipeline steps to file.

        param out_path: Where files should go
        """
        if self.img_pipeline is None:
            raise ValueError("Cannot save when img_pipeline=None.")
        self.img_pipeline.save_output(out_path=out_path)

    def run_on_images(
        self, images_dir: str, mechanism: str = "sequential"
    ) -> Union[List[str], List[List[str]]]:
        """
        API to run OCR on a directory of images.

        param files_path: Path to directory of card image files

        return:
            output: List of OCR results
        """
        files = natsorted(
            [
                os.path.join(images_dir, file)
                for file in os.listdir(images_dir)
                if sys_util.is_image_file(file_path=file)
            ]
        )
        results = paraloop.loop(
            func=self.run_on_img_file, params=files, mechanism=mechanism
        )
        return results
