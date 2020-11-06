from Lib.Connectors import PriceFileConverter
import sys


class Range(PriceFileConverter.PriceFileConverter):

    def __init__(self, config_folder, config_file, input_folder, output_folder,  parse):
        super().__init__(config_folder, config_file, input_folder, output_folder, parse)

    def parse_file_name(self, file_name):
        """
        Parse a Dukascopy Range File name into
        internal format

        :return:
        """

        _comps = str(file_name).split("_")
        _fn_info = dict()
        _fn_info["represent"] = "RANGE"
        _fn_info["instrument"] = _comps[0]
        _fn_info["bar_size"] = _comps[2]
        _fn_info["price_type"] = _comps[4]
        assert _fn_info["price_type"].lower() in ["bid", "ask"], \
            f"wrong price type {_fn_info['price_type']}, must be Bid or Ask"

        if _fn_info["bar_size"] == "ONE":
            _fn_info["bar_size"] = "1"
        elif _fn_info["bar_size"] == "TWO":
            _fn_info["bar_size"] = "2"
        elif _fn_info["bar_size"] == "FIVE":
            _fn_info["bar_size"] = "5"

        self.file_name_info = _fn_info

        return _fn_info

if __name__ == "__main__":
    try:
        _config_folder = sys.argv[1]
        _config_file = sys.argv[2]
        _input_folder = sys.argv[3]
        _output_folder = sys.argv[4]

    except Exception as e:
        raise Exception(str(e))

    print("Processing for", _config_file)

    _rk = Range(_config_folder, _config_file, _input_folder, _output_folder, "")
    _rk.run()
