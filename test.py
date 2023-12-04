from oauth2client.tools import argparser

argparser.add_argument("--file", required=True,
                        help="Video file to upload")

args = argparser.parse_args()

print(type(args))

print(args)