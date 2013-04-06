#!/usr/bin/python
# -*- coding: utf8 -*-

import os
import sys
import getopt
from player import exception as pException
from command import exception as CommandException
from Rpg import Rpg
from argparse import ArgumentParser


def main(argv):
	parser = ArgumentParser()

	parser.add_argument(
		"-l", "--login",
		dest="login", help="Player login", metavar="LOGIN"
	)
	parser.add_argument(
		"-p", "--password",
		dest="password", help="Player password", metavar="PASSWORD"
	)
	parser.add_argument(
		"action",
		metavar="A", nargs='*', help="Action to execute"
	)

	args = parser.parse_args()

	try:
		rpg = Rpg(args.login, args.password, args.action)
		rpg.run()
	except CommandException as e:
		print(e)
		sys.exit()
	except pException as e:
		print(e)
		sys.exit()
	except KeyboardInterrupt:
		sys.exit()
	except BaseException as e:
		print(e)
		sys.exit()

if __name__ == "__main__":
	main(sys.argv[1:])
