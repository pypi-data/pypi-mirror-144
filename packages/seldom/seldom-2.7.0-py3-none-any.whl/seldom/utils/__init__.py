import os
import sys
import inspect


class FindFilePath:

    def __new__(cls, name) -> str:
        if name is None:
            raise NameError("Please specify filename")
        stack_t = inspect.stack()
        ins = inspect.getframeinfo(stack_t[1][0])
        this_file_dir = os.path.dirname(os.path.dirname(os.path.abspath(ins.filename)))

        _file_path = None
        for root, dirs, files in os.walk(this_file_dir, topdown=False):
            for file in files:
                if file == name:
                    _file_path = os.path.join(root, file)
                    break
            else:
                continue
            break
        return _file_path


find_file_path = FindFilePath


class File:

    @property
    def path(self) -> str:
        """
        Returns the absolute path to the directory where the current file resides
        For example:
            "/User/tech/you/test_dir/test_sample.py"
            return "/User/tech/you/test_dir/test_sample.py"
        """
        stack_t = inspect.stack()
        ins = inspect.getframeinfo(stack_t[1][0])
        return os.path.abspath(ins.filename)

    @property
    def dir(self) -> str:
        """
        Returns the absolute path to the directory where the current file resides
        For example:
            "/User/tech/you/test_dir/test_sample.py"
            return "/User/tech/you/test_dir/"
        """
        stack_t = inspect.stack()
        ins = inspect.getframeinfo(stack_t[1][0])
        return os.path.dirname(os.path.abspath(ins.filename))

    @property
    def dir_dir(self) -> str:
        """
        Returns the absolute directory path of the current file directory.
        For example:
            "/User/tech/you/test_dir/test_sample.py"
            return "/User/tech/you/"
        """
        stack_t = inspect.stack()
        ins = inspect.getframeinfo(stack_t[1][0])
        return os.path.dirname(os.path.dirname(os.path.abspath(ins.filename)))

    @property
    def dir_dir_dir(self) -> str:
        """
        Returns the absolute directory path of the current file directory
        For example:
            /User/tech/you/test_dir/test_sample.py
            return "/User/you/"
        """
        stack_t = inspect.stack()
        ins = inspect.getframeinfo(stack_t[1][0])
        return os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(ins.filename))))

    @staticmethod
    def add_to_path(path=None) -> None:
        """
        add path to environment variable path.
        """
        if path is None:
            raise FileNotFoundError("Please setting the File Path")

        sys.path.insert(1, path)


file = File()


class AssertInfo:
    data = []


def diff_json(response_data, assert_data):
    """
    Compare the JSON data format
    """
    if isinstance(response_data, dict):
        """ dict format """
        for key in assert_data:
            if key not in response_data:
                info = "❌ Response data has no key: {}".format(key)
                print(info)
                AssertInfo.data.append(info)
        for key in response_data:
            if key in assert_data:
                """ recursion """
                diff_json(response_data[key], assert_data[key])
            else:
                info = "💡 Assert data has not key: {}".format(key)
                print(info)
    elif isinstance(response_data, list):
        """ list format """
        if len(response_data) == 0:
            print("response is []")
        else:
            if isinstance(response_data[0], dict):
                response_data = sorted(response_data, key=lambda x: x[list(response_data[0].keys())[0]])
            else:
                response_data = sorted(response_data)

        if len(response_data) != len(assert_data):
            print("list len: '{}' != '{}'".format(len(response_data), len(assert_data)))

        if len(assert_data) > 0:
            if isinstance(assert_data[0], dict):
                assert_data = sorted(assert_data, key=lambda x: x[list(assert_data[0].keys())[0]])
            else:
                assert_data = sorted(assert_data)

        for src_list, dst_list in zip(response_data, assert_data):
            """ recursion """
            diff_json(src_list, dst_list)
    else:
        if str(response_data) != str(assert_data):
            info = "❌ Value are not equal: {}".format(response_data)
            print(info)
            AssertInfo.data.append(info)


