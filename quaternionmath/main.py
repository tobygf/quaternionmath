# quaternionmath
# Provides a "Quaternion" class for adding, subtracting, multiplying,
# and dividing Quaternion numbers. 
# V 1.0

class Quaternion():
    """
    Class defining the Quaternion (four-dimensional) numbers.
    """
    def __init__(self, *args):
        """
        Constructor method for Quaternion class.

        Can take the following argument combinations:
        1-4 ints/floats.
        1 complex.
        1 Quaternion.
        """
        # Constructs a Quaternion based on a single complex number.
        if len(args) == 1 and type(args[0]) == complex:
            # The real and imaginary parts of a complex number
            # correspond with "a" and "b" of a Quaternion.
            self.a = args[0].real
            self.b = args[0].imag
            # The third and fourth parts equate to zero, as complex numbers
            # have only two parts.
            self.c = 0.0
            self.d = 0.0

        # Constructs a Quaternion based on up to 4 numbers, which
        # correspond with "a", "b", "c", and "d".
        elif (0 < len(args) < 5
              and all(isinstance(i, int)
                  or isinstance(i, float) for i in args)):

            # Tries to set each Quaternion part to corresponding argument,
            # and if that fails, sets it to zero.
            try:
                self.a = float(args[0])
            except:
                self.a = 0.0
            try:
                self.b = float(args[1])
            except:
                self.b = 0.0
            try:
                self.c = float(args[2])
            except:
                self.c = 0.0
            try:
                self.d = float(args[3])
            except:
                self.d = 0.0

        # Clones an exisiting Quaternion
        elif len(args) == 1 and isinstance(args[0], Quaternion):
            self.a = args[0].a
            self.b = args[0].b
            self.c = args[0].c
            self.d = args[0].d

    def __add__(self, other):
        """
        Quaternion addition method.

        Args:
        other -- Quaternion/int/float/complex to add to Quaternion.
        
        Returns:
        Result of additon operation, as a Quaternion object.
        """
        if (isinstance(other, int)
            or isinstance(other, float)
                or isinstance(other, complex)
                    or isinstance(other, Quaternion)):
            # Adds each pair of Quaternion parts seperately
            result = Quaternion(self)
            other = Quaternion(other)
            result.a += other.a
            result.b += other.b
            result.c += other.c
            result.d += other.d
            return(result)
        else:
            # Returns NotImplemented if illegal paramter passed.
            return NotImplemented

    def __radd__(self, other):
        """
        Quaternion reversed addition method.

        Args:
        other -- Quaternion/int/float/complex to add Quaternion to.
        
        Returns:
        Either:
        Result of additon operation, as a Quaternion object, or
        NotImplemented.
        """
        if (isinstance(other, int)
            or isinstance(other, float)
                or isinstance(other, complex)
                    or isinstance(other, Quaternion)):
            # Adds each pair of Quaternion parts seperately
            result = Quaternion(self)
            other = Quaternion(other)
            result.a += other.a
            result.b += other.b
            result.c += other.c
            result.d += other.d
            return(result)
        else:
            # Returns NotImplemented if illegal paramter passed.
            return NotImplemented

    def __sub__(self, other):
        """
        Quaternion subtraction method.

        Args:
        other -- Quaternion/int/float/complex to subtract from Quaternion.

        Returns:
        Result of subtraction operation, as a Quaternion object.
        """
        if (isinstance(other, int)
            or isinstance(other, float)
                or isinstance(other, complex)
                    or isinstance(other, Quaternion)):
            result = Quaternion(other)
            # Subtracts from each Quaternion part seperately
            result.a -= self.a
            result.b -= self.b
            result.c -= self.c
            result.d -= self.d
            return(result)
        else:
            # Returns NotImplemented if illegal paramter passed.
            return NotImplemented

    def __rsub__(self, other):
        """
        Quaternion reversed subtraction method.

        Args:
        other -- Quaternion/int/float/complex to subtract Quaternion from.

        Returns:
        Result of subtraction operation, as a Quaternion object.
        """
        if (isinstance(other, int)
            or isinstance(other, float)
                or isinstance(other, complex)
                    or isinstance(other, Quaternion)):
            result = Quaternion(self)
            other = Quaternion(other)
            # Subtracts from each Quaternion part seperately
            result.a -= other.a
            result.b -= other.b
            result.c -= other.c
            result.d -= other.d
            return(result)
        else:
            # Returns NotImplemented if illegal paramter passed.
            return NotImplemented

    def __mul__(self, other):
        """
        Quaternion multiplication method.

        Args:
        other -- Quaternion/int/float/complex to multiply Quaternion by.

        Returns:
        Result of multiplication operation, as a Quaternion object.
        """
        if (isinstance(other, int)
            or isinstance(other, float)
                or isinstance(other, complex)
                    or isinstance(other, Quaternion)):
            # Applies quaternion multiplication table, getting each part of
            # the resulting Quaternion.
            atotal = ((self.a * other.a) - (self.b * other.b)
                      - (self.c * other.c) - (self.d * other.d))
            btotal = ((self.a * other.b) + (self.b * other.a)
                      + (self.c * other.d) - (self.d * other.c))
            ctotal = ((self.a * other.c) - (self.b * other.d)
                      + (self.c * other.a) + (self.d * other.b))
            dtotal = ((self.a * other.d) + (self.b * other.c)
                      - (self.c * other.b) + (self.d * other.a))
            result = Quaternion(atotal, btotal, ctotal, dtotal)
            return result
        else:
            # Returns NotImplemented if illegal paramter passed.
            return NotImplemented

    def __rmul__(self, other):
        """
        Quaternion reversed multiplication method.

        Args:
        other -- Quaternion/int/float/complex to multiply by Quaternion.

        Returns:
        Result of multiplication operation, as a Quaternion object.
        """
        if (isinstance(other, int)
            or isinstance(other, float)
                or isinstance(other, complex)
                    or isinstance(other, Quaternion)):
            other = Quaternion(other)
            # Applies quaternion multiplication table, getting each part of
            # the resulting Quaternion.
            atotal = ((other.a * self.a) - (other.b * self.b)
                      - (other.c * self.c) - (other.d * self.d))
            btotal = ((other.a * self.b) + (other.b * self.a)
                      + (other.c * self.d) - (other.d * self.c))
            ctotal = ((other.a * self.c) - (other.b * self.d)
                      + (other.c * self.a) + (other.d * self.b))
            dtotal = ((other.a * self.d) + (other.b * self.c)
                      - (other.c * self.b) + (other.d * self.a))
            result = Quaternion(atotal, btotal, ctotal, dtotal)
            return result
        else:
            # Returns NotImplemented if illegal paramter passed.
            return NotImplemented

    def __truediv__(self, other):
        """
        Quaternion division method

        Args:
        other -- Quaternion/int/float/complex to divide Quaternion by.

        Returns:
        Result of multiplication operation, as a Quaternion object.
        """
        if (isinstance(other, int)
            or isinstance(other, float)
                or isinstance(other, complex)
                    or isinstance(other, Quaternion)):
            other = Quaternion(other)
            # All parts are divided by this common denominator
            denominator = ((other.a**2) + (other.b**2)
                           + (other.c**2) + (other.d**2))
            # Applies formula to get each part of the resulting Quaternion.
            atotal = ((self.a * other.a) + (self.b * other.b)
                      + (self.c * other.c) + (self.d * other.d))/denominator
            btotal = ((self.b * other.a) - (self.a * other.b)
                      - (self.d * other.c) + (self.c * other.d))/denominator
            ctotal = ((self.c * other.a) + (self.d * other.b)
                      - (self.a * other.c) - (self.b * other.d))/denominator
            dtotal = ((self.d * other.a) - (self.c * other.b)
                      + (self.b * other.c) - (self.a * other.d))/denominator
            result = Quaternion(atotal, btotal, ctotal, dtotal)
            return result
        else:
            # Returns NotImplemented if illegal paramter passed.
            return NotImplemented

    def __rtruediv__(self, other):
        """
        Quaternion division method

        Args:
        other -- Quaternion/int/float/complex to divide by Quaternion.

        Returns:
        Result of multiplication operation, as a Quaternion object.
        """
        if (isinstance(other, int)
            or isinstance(other, float)
                or isinstance(other, complex)
                    or isinstance(other, Quaternion)):
            other = Quaternion(other)
            # All parts are divided by this common denominator
            denominator = (self.a**2) + (self.b**2) + (self.c**2) + (self.d**2)
            # Applies formula to get each part of the resulting Quaternion.
            atotal = ((other.a * self.a) + (other.b * self.b)
                      + (other.c * self.c) + (other.d * self.d))/denominator
            btotal = ((other.b * self.a) - (other.a * self.b)
                      - (other.d * self.c) + (other.c * self.d))/denominator
            ctotal = ((other.c * self.a) + (other.d * self.b)
                      - (other.a * self.c) - (other.b * self.d))/denominator
            dtotal = ((other.d * self.a) - (other.c * self.b)
                      + (other.b * self.c) - (other.a * self.d))/denominator
            result = Quaternion(atotal, btotal, ctotal, dtotal)
            return result
        else:
            # Returns NotImplemented if illegal paramter passed.
            return NotImplemented

    def __div__(self, other):
        """
        Quaternion division method

        Args:
        other -- Quaternion/int/float/complex to divide Quaternion by.

        Returns:
        Result of multiplication operation, as a Quaternion object.
        """
        if (isinstance(other, int)
            or isinstance(other, float)
                or isinstance(other, complex)
                    or isinstance(other, Quaternion)):
            other = Quaternion(other)
            # All parts are divided by this common denominator
            denominator = ((other.a**2) + (other.b**2)
                           + (other.c**2) + (other.d**2))
            # Applies formula to get each part of the resulting Quaternion.
            atotal = ((self.a * other.a) + (self.b * other.b)
                      + (self.c * other.c) + (self.d * other.d))/denominator
            btotal = ((self.b * other.a) - (self.a * other.b)
                      - (self.d * other.c) + (self.c * other.d))/denominator
            ctotal = ((self.c * other.a) + (self.d * other.b)
                      - (self.a * other.c) - (self.b * other.d))/denominator
            dtotal = ((self.d * other.a) - (self.c * other.b)
                      + (self.b * other.c) - (self.a * other.d))/denominator
            result = Quaternion(atotal, btotal, ctotal, dtotal)
            return result
        else:
            # Returns NotImplemented if illegal paramter passed.
            return NotImplemented

    def __rdiv__(self, other):
        """
        Quaternion division method

        Args:
        other -- Quaternion/int/float/complex to divide by Quaternion.

        Returns:
        Result of multiplication operation, as a Quaternion object.
        """
        if (isinstance(other, int)
            or isinstance(other, float)
                or isinstance(other, complex)
                    or isinstance(other, Quaternion)):
            other = Quaternion(other)
            # All parts are divided by this common denominator
            denominator = (self.a**2) + (self.b**2) + (self.c**2) + (self.d**2)
            # Applies formula to get each part of the resulting Quaternion.
            atotal = ((other.a * self.a) + (other.b * self.b)
                      + (other.c * self.c) + (other.d * self.d))/denominator
            btotal = ((other.b * self.a) - (other.a * self.b)
                      - (other.d * self.c) + (other.c * self.d))/denominator
            ctotal = ((other.c * self.a) + (other.d * self.b)
                      - (other.a * self.c) - (other.b * self.d))/denominator
            dtotal = ((other.d * self.a) - (other.c * self.b)
                      + (other.b * self.c) - (other.a * self.d))/denominator
            result = Quaternion(atotal, btotal, ctotal, dtotal)
            return result
        else:
            # Returns NotImplemented if illegal paramter passed.
            return NotImplemented

    def __eq__(self, other):
        """
        Quaternion '==' or eq method.

        Args:
        other -- Quaternion/int/float/complex to determine equality
        with Quatenrion.

        Returns:
        Boolean, signifying whether self and other are equal.
        """
        if (isinstance(other, int)
            or isinstance(other, float)
                or isinstance(other, complex)
                    or isinstance(other, Quaternion)):
            other = Quaternion(other)
            # Determines whether each part of self is equal to each part of
            # other.
            return(self.a == other.a and self.b == other.b
                   and self.c == other.c and self.d == other.d)
        else:
            # Returns NotImplemented if illegal paramter passed.
            return NotImplemented

    def __req__(self, other):
        """
        Quaternion reversed '==' or eq method.

        Args:
        other -- Quaternion/int/float/complex to determine equality
        with Quatenrion.

        Returns:
        Boolean, signifying whether self and other are equal.
        """
        if (isinstance(other, int)
            or isinstance(other, float)
                or isinstance(other, complex)
                    or isinstance(other, Quaternion)):
            other = Quaternion(other)
            # Determines whether each part of self is equal to each part of
            # other.
            return(self.a == other.a and self.b == other.b
                   and self.c == other.c and self.d == other.d)
        else:
            # Returns NotImplemented if illegal paramter passed.
            return NotImplemented

    def __repr__(self):
        """
        Quaternion representation - should be intelligible by eval function.

        Returns:
        A string, which when passed to eval will give back the Quatenrion
        object.
        """

        return ("quaternionmath.Quaternion(" + str(self.a) + ", " + str(self.b)
                + ", " + str(self.c) + ", " + str(self.d) + ")")

    def __str__(self):
        """
        Quaternion string form.

        Returns:
        A string expressing the value of the Quaternion - should be
        user-readable.
        """
        # Expresses Quaternion in "a + bi + cj + dk" notation
        string = (str(self.a) + " + " + str(self.b)
                  + "i + " + str(self.c) + "j + " + str(self.d) + "k")
        return(string)
