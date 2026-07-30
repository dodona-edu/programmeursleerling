class CourseSetChecker(OutputProcessor):

    """
    Compares the set of courses returned by the submission with the set of
    courses that was expected. Both sets are compared as sorted lists of the
    string representations of the courses they contain, and are also shown that
    way in the feedback table. Two reasons for not comparing the sets of courses
    themselves:

      - the judge deep copies the expected value before comparing it, so the
        expected set holds other course objects than the ones the submission
        put in its own set; comparing the sets themselves would then only
        succeed if the submission defines equality and hashing on its course
        class, which this exercise doesn't ask for (chapter 21)
      - a set has no fixed iteration order, so the order in which the courses
        of the expected and the generated set show up in the feedback table
        would otherwise be arbitrary and could differ between both sets

    Comparing the string representations is safe here, since the exercise
    already requires the representation of a course to hold both its identifier
    and its name, and a separate tab checks that representation.
    """

    def representations(self, courses):

        # sorted list of the string representations of the given courses
        return sorted(repr(course) for course in courses)

    def format(self, courses):

        # set notation with the courses in the order in which they are compared
        if not courses:
            return 'set()'

        return '{' + ', '.join(self.representations(courses)) + '}'

    def checkReturnValue(self, expected_return, generated_return, **parameters):

        if not (
            isinstance(expected_return, set) and
            isinstance(generated_return, set)
        ):

            # fall back on the default comparison if no set of courses was
            # returned; the type check has already reported that error
            return super().checkReturnValue(
                expected_return,
                generated_return,
                **parameters
            )

        # show both sets of courses in the order in which they are compared, so
        # that a missing or a superfluous course is easy to spot
        self.setOutput(
            channel='return',
            expected=[self.format(expected_return)],
            generated=[self.format(generated_return)],
            split=True,
            escaped=False
        )

        return (
            self.representations(expected_return) ==
            self.representations(generated_return)
        )
