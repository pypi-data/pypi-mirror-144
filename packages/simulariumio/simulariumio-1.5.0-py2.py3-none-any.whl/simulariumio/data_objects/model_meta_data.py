#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Dict, Any
import logging

###############################################################################

log = logging.getLogger(__name__)

###############################################################################


class ModelMetaData:
    title: str
    version: str
    authors: str
    description: str
    doi: str
    source_code_url: str
    source_code_license_url: str
    input_data_url: str
    raw_output_data_url: str

    def __init__(
        self,
        title: str = "",
        version: str = "",
        authors: str = "",
        description: str = "",
        doi: str = "",
        source_code_url: str = "",
        source_code_license_url: str = "",
        input_data_url: str = "",
        raw_output_data_url: str = "",
    ):
        """
        This object holds metadata for a model that generates simulation trajectories
        Parameters
        ----------
        title : str (optional)
            Display title for this model
        version : float (optional)
            Version number of the model that produced this trajectory
        authors : str (optional)
            Modelers name(s)
        description : str (optional)
            Comments to display with the trajectories generated by this model
        doi : str (optional)
            The DOI of the publication accompanying this model
            Note: if the URL for a DOI is provided,
                the ID from the URL will be used
        source_code_url : str (optional)
            If the code that generated this model is posted publicly,
            a link to the repository of source code
        source_code_license_url : str (optional)
            A link to the license for the source code
        input_data_url : str (optional)
            A link to any model configuration or parameter files posted publicly
        raw_output_data_url : str (optional)
            A link to any raw outputs from the source code posted publicly
        """
        self.title = title
        self.version = version
        self.authors = authors
        self.description = description
        # remove url prefix from doi
        if "doi.org" in doi:
            doi = doi[doi.index("doi.org") + 8 :]
        self.doi = doi
        self.source_code_url = source_code_url
        self.source_code_license_url = source_code_license_url
        self.input_data_url = input_data_url
        self.raw_output_data_url = raw_output_data_url

    @classmethod
    def from_buffer_data(cls, buffer_data: Dict[str, Any]):
        """
        Create ModelMetaData from a simularium JSON dict containing buffers
        """
        model_info = (
            buffer_data["trajectoryInfo"]["modelInfo"]
            if "modelInfo" in buffer_data["trajectoryInfo"]
            else None
        )
        if model_info is None:
            return cls()
        return cls(
            title=model_info["title"] if "title" in model_info else "",
            version=model_info["version"] if "version" in model_info else "",
            authors=model_info["authors"] if "authors" in model_info else "",
            description=model_info["description"]
            if "description" in model_info
            else "",
            doi=model_info["doi"] if "doi" in model_info else "",
            source_code_url=model_info["sourceCodeUrl"]
            if "sourceCodeUrl" in model_info
            else "",
            source_code_license_url=model_info["sourceCodeLicenseUrl"]
            if "sourceCodeLicenseUrl" in model_info
            else "",
            input_data_url=model_info["inputDataUrl"]
            if "inputDataUrl" in model_info
            else "",
            raw_output_data_url=model_info["rawOutputDataUrl"]
            if "rawOutputDataUrl" in model_info
            else "",
        )

    def is_default(self):
        """
        Check if this ModelMetaData is only holding default data
        """
        return (
            not self.title
            and not self.version
            and not self.authors
            and not self.description
            and not self.doi
            and not self.source_code_url
            and not self.source_code_license_url
            and not self.input_data_url
            and not self.raw_output_data_url
        )

    def __iter__(self):
        if self.title:
            yield "title", self.title
        if self.version:
            yield "version", self.version
        if self.authors:
            yield "authors", self.authors
        if self.description:
            yield "description", self.description
        if self.doi:
            yield "doi", self.doi
        if self.source_code_url:
            yield "sourceCodeUrl", self.source_code_url
        if self.source_code_license_url:
            yield "sourceCodeLicenseUrl", self.source_code_license_url
        if self.input_data_url:
            yield "inputDataUrl", self.input_data_url
        if self.raw_output_data_url:
            yield "rawOutputDataUrl", self.raw_output_data_url
