"""Missing field error
"""


class RelevanceAIError(Exception):
    """_Base class for all errors"""


class MissingFieldError(RelevanceAIError):
    """Error handling for missing fields"""


class APIError(RelevanceAIError):
    """Error related to API"""


class ClusteringResultsAlreadyExistsError(RelevanceAIError):
    """Exception raised for existing clustering results

    Attributes:
        message -- explanation of the error
    """

    def __init__(
        self, field_name, message="""Clustering results for %s already exist"""
    ):
        self.field_name = field_name
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message % (self.field_name)


class NoDocumentsError(RelevanceAIError):
    """Error for when no documents are retrieved for an operation."""

    def __init__(self, message="""No documents were found."""):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message
