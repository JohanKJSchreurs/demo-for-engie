"""Command line interface of the Hello World application."""

import argparse
import sys


class CLIHelloWorld:
    """The command line interface for the Hello World application.

    Making this a class though it could have been a simple procedural script,
    but a class like this makes it a little bit easier to write unit tests
    for the program.

    Futher, it allows us to set up the database connection and the
    argument parser only once, in the constructor.
    """

    def __init__(self):
        self._parser = CLIHelloWorld.create_parser()

        # TODO: add something that will connect to the database and get the name corresponds to the ID.

    @classmethod
    def create_parser(cls):
        """Create an argument parser with the necessary options."""

        description = ("Display the hello message with the name that " +
                       "corresponds to the ID in the database.")
        parser = argparse.ArgumentParser(description=description)
        parser.add_argument(
            "id", type=int,
            help="The numerical ID of the person in the database."
        )
        return parser

    def run(self, argv):
        """Run the command line interface."""

        # You can pass your own arguments to the method rather than using
        # sys.argv, which mainly meant for testing.
        # This way you can simulate specific arguments in an automated test.
        if argv is None:
            argv = sys.argv

        arguments = self._parser.parse_args()
        person_id = arguments.id

        if person_id is None:
            print("ERROR: No ID specified. Please try again and specify a numerical ID.\n")
            self._parser.print_help()
        elif person_id < 0:
            print("ERROR: ID can not be a negative number. Please try again with a positive number.\n")
            self._parser.print_help()
        else:
            self.show_name(arguments.id)

    def show_name(self, person_id: int):
        """Show the name that corresponds to the person_id in the database."""

        if person_id < 0:
            raise ValueError("person_id can not be a negative number")

        name = self.get_name_for_id(person_id)
        print(f"Hello {name}!")

    def get_name_for_id(self, person_id: int):
        """Get the name that corresponds to person_id from the database."""

        # TODO: this is a stub/fake implementation
        # TODO: error handling when there is no person with the requested person_id.
        print("This is a placeholder. Not implemented yet")
        print(f"Looking up person_id: {person_id}")
        return f"name for {person_id}"


def main():
    """Main program of the CLI interface.
    Launches the program with the commandline arguments passed to the program.

    """
    cli = CLIHelloWorld()
    cli.run(sys.argv)


# Only run the program if the module is being run as a script.
# This prevents that the program runs when you just import the module,
# for example in a unit test.
if __name__ == "__main__":
    main()
