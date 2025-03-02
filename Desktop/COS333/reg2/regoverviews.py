"""
Registrar Application

This script connects to a registrar server and retrieves class overviews
based on various filters such as department, course number, distribution
area, and course title.
"""

import sys
import argparse
import socket
import json
import textwrap


def parse_args():
    """Parse command line arguments.

    Returns:
        argparse.Namespace: Parsed command line arguments
    """
    parser = argparse.ArgumentParser(
        description="Registrar application: show overviews of classes")

    parser.add_argument("host", help="the computer on which the server is running")
    parser.add_argument("port", help="the port at which the server is listening", type=int)
    parser.add_argument("-d", metavar="dept",
                        help="show only those classes whose department contains dept")
    parser.add_argument("-n", metavar="num",
                        help="show only those classes whose course number contains num")
    parser.add_argument("-a", metavar="area",
                        help="show only those classes whose distrib area contains area")
    parser.add_argument("-t", metavar="title",
                        help="show only those classes whose course title contains title")

    return parser.parse_args()


def get_overviews(host, port, filters):
    """Connect to the server and get class overviews.

    Args:
        host (str): Server hostname or IP address
        port (int): Server port number
        filters (dict): Dictionary of filtering parameters

    Returns:
        list: List of dictionaries containing class data

    Raises:
        SystemExit: If there's an error connecting to the server
    """
    request = ["get_overviews", filters]

    try:
        with socket.socket() as sock:
            sock.connect((host, port))
            sock.sendall((json.dumps(request) + '\n').encode())

            response_data = ""
            while True:
                data = sock.recv(4096).decode()
                if not data:
                    break
                response_data += data
                if response_data.endswith('\n'):
                    break

            response = json.loads(response_data)

            if not response[0]:
                print(f"regoverviews: {response[1]}", file=sys.stderr)
                sys.exit(1)

            return response[1]

    except (socket.error, json.JSONDecodeError) as ex:
        print(f"regoverviews: {ex}", file=sys.stderr)
        sys.exit(1)


def format_output(classes):
    """Format the output as a table with wrapped text.

    Args:
        classes (list): List of dictionaries containing class data
    """
    print("ClsId Dept CrsNum Area Title")
    print("----- ---- ------ ---- -----")

    if classes:
        for class_info in classes:
            classid = class_info['classid']
            dept = class_info['dept']
            coursenum = class_info['coursenum']
            area = class_info['area']
            title = class_info['title']

            line = f"{classid:>5} {dept:>4} {coursenum:>6} {area:>4} {title}"
            wrapped = textwrap.wrap(line, width=72, subsequent_indent=' ' * 23)
            print('\n'.join(wrapped))


def main():
    """Main function to run the program."""
    args = parse_args()

    filters = {
        "dept": args.d if args.d else "",
        "coursenum": args.n if args.n else "",
        "area": args.a if args.a else "",
        "title": args.t if args.t else ""
    }

    try:
        classes = get_overviews(args.host, args.port, filters)
        format_output(classes)
        sys.exit(0)
    except (socket.error, json.JSONDecodeError) as ex:
        print(f"regoverviews: {str(ex)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
