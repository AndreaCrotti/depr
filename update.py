#!/usr/bin/env python

import argparse
import git
import semantic_version


NEXT_MAPPING = {
    'major': semantic_version.Version.next_major,
    'minor': semantic_version.Version.next_minor,
    'patch': semantic_version.Version.next_patch,
}


def parse_arguments():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-m', '--mode',
                        choices=('major', 'minor', 'patch'),
                        default='patch')

    parser.add_argument('-p', '--publish',
                        action='store_true')

    return parser.parse_args()


def main():
    args = parse_arguments()
    repo = git.Repo('.')
    # TODO: move the git.Repo somewhere else?
    current = semantic_version.Version(repo.tags[-1].name)
    new_version = NEXT_MAPPING[args.mode](current)
    print("Creating new tag {}".format(new_version))
    # repo.tag(str(new_version))


if __name__ == '__main__':
    main()
