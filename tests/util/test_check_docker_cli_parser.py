import unittest
import sys
from dagda.util.check_docker_cli_parser import CheckDockerCLIParser


# -- Test suite

class CheckDockerImageCLIParserTestSuite(unittest.TestCase):

    def test_empty_args(self):
        empty_args = generate_args(None, None)
        status = CheckDockerCLIParser.verify_args("check_docker.py", empty_args)
        self.assertEqual(status, 1)

    def test_both_arguments(self):
        args = generate_args('jboss/wildfly', '43a6ca974743')
        status = CheckDockerCLIParser.verify_args("check_docker.py", args)
        self.assertEqual(status, 2)

    def test_ok_only_image_name(self):
        args = generate_args('jboss/wildfly', None)
        status = CheckDockerCLIParser.verify_args("check_docker.py", args)
        self.assertEqual(status, 0)

    def test_ok_only_container_id(self):
        args = generate_args(None, '43a6ca974743')
        status = CheckDockerCLIParser.verify_args("check_docker.py", args)
        self.assertEqual(status, 0)

    def test_check_full_happy_path(self):
        sys.argv = ['check_docker.py', '-i', 'jboss/wildfly']
        parsed_args = CheckDockerCLIParser()
        self.assertEqual(parsed_args.get_docker_image_name(), 'jboss/wildfly')


# -- Util methods

def generate_args(docker_image, container_id):
    return AttrDict([('container_id', container_id), ('docker_image', docker_image)])


# -- Util classes

class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


if __name__ == '__main__':
    unittest.main()
