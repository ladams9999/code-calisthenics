


class Month():

    def __init__(self, month_id:str, metrics:dict):
        """_summary_

        Args:
        month_id (str): _description_
        metrics (dict): _description_
        """
        self.id = month_id
        self.metrics = metrics

    def get_metric(self, metric:str):
        """_summary_

        Args:
            metric (str): _description_

        Returns:
            _type_: _description_
        """
        if metric in self.metrics:
            return self.metrics[metric]
        else:
            # TODO:Error handling
            return ""