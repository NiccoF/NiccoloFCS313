"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Niccolo Faelnar, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: nvf89
UT EID 2:
"""


class Node:
    """
    A modified version of the Node class for linked lists (using proper class
    coding practices). Instead of a data instance variable, this node class has both
    a coefficient and an exponent instance variable, which is used to represent each
    term in a polynomial.
    """

    def __init__(self, coeff, exp, link=None):
        """
        Node Constructor for polynomial linked lists.

        Args:
        - coeff: The coefficient of the term.
        - exp: The exponent of the term.
        - link: The next node in the linked list.
        """
        self.coeff = coeff
        self.exp = exp
        self.next = link

    @property
    def coeff(self):
        """
        Getter method for the coefficient attribute.
        """
        return self.__coeff

    @coeff.setter
    def coeff(self, value):
        """
        Setter method for the coefficient attribute.
        """
        if value is None or isinstance(value, int):
            self.__coeff = value
        else:
            raise ValueError("Coefficient must be an integer or None.")

    @property
    def exp(self):
        """
        Getter method for the exponent attribute.
        """
        return self.__exp

    @exp.setter
    def exp(self, value):
        """
        Setter method for the exponent attribute.
        """
        if value is None or isinstance(value, int):
            self.__exp = value
        else:
            raise ValueError("Exponent must be an integer or None.")

    @property
    def next(self):
        """
        Getter method for the next attribute.
        """
        return self.__next

    @next.setter
    def next(self, value):
        """
        Setter method for the next attribute.
        """
        if value is None or isinstance(value, Node):
            self.__next = value
        else:
            raise ValueError("Next must be a Node instance or None.")

    def __str__(self):
        """
        String representation of each term in a polynomial linked list.
        """
        return f"({self.coeff}, {self.exp})"


class LinkedList:
    def __init__(self):
        # You are also welcome to use a sentinel/dummy node!
        # It is definitely recommended, which will we learn more
        # about in class on Monday 10/21. If you choose to use
        # a dummy node, you can comment out the self.head = None
        # and comment in the below line. We use None to make sure
        # if there is an error where you accidentally include the
        # dummy node in your calculation, it will throw an error.
        self.dummy = Node(None, None)
        # self.head = None

    # If a term with that exponent already exists, add the coefficients together.
    # You must keep the terms in descending order by exponent.
    def insert_term(self, coeff, exp):
        '''Inserts the term with the coefficient coeff and exponent exp into the polynomial.
        '''
        if(coeff == 0 or exp < 0):
            return
        current = self.dummy.next
        previous = self.dummy
        # Iterate till current exp <= input exp
        while current is not None:
            if current.exp <= exp:
                break
            previous = current
            current = current.next
        # If end of list add the term at the end
        if current is None:
            node = Node(coeff, exp, current)
            previous.next = node
            return
        # If same exp then add coeff
        if current.exp is exp:
            current.coeff += coeff
            # if the coeff is 0 then remove it from the list
            if current.coeff == 0:
                previous.next = current.next
            return
        # If hit a term with its exp < exp or end, add the new term before it
        node = Node(coeff, exp, current)
        previous.next = node
        return

    # Add a polynomial p to the polynomial and return the resulting polynomial as a new linked list.
    def add(self, p):
        return_list = LinkedList()
        current = p.dummy.next
        # Iterate whole p list
        while current is not None:
            return_list.insert_term(current.coeff, current.exp)
            current = current.next
        current = self.dummy.next
        # Iterate whole self list
        while current is not None:
            return_list.insert_term(current.coeff, current.exp)
            current = current.next
        return return_list

    # Multiply a polynomial p with the polynomial and return the product as a new linked list.
    def mult(self, p):
        new_list = LinkedList()
        current = self.dummy.next
        # previous = self.dummy

        # Iterate whole list
        while current is not None:
            p_current = p.dummy.next
            # p_previous = p.dummy
            while p_current is not None:
                new_list.insert_term(
                    (current.coeff * p_current.coeff),
                    (current.exp + p_current.exp)
                    )
                # p_previous = p_current
                p_current = p_current.next
            # previous = current
            current = current.next
        return new_list

    # Return a string representation of the polynomial.
    def __str__(self):
        # Skip first element
        return_string = ""
        if self.dummy.next is not None:
            return_string += str(self.dummy.next)
            current = self.dummy.next.next
            while current is not None:
                return_string += " + " + str(current)
                current = current.next
        return return_string


def main():
    # read data from stdin using input() and create polynomial p

    # read data from stdin using input() and create polynomial q

    # get sum of p and q as a new linked list and print sum

    # get product of p and q as a new linked list and print product
    p = LinkedList()
    n = int(input())
    for i in range(n):
        next_line = input()
        coeff_and_exp = next_line.split(" ")
        p.insert_term(int(coeff_and_exp[0]), int(coeff_and_exp[1]))
    input()
    q = LinkedList()
    m = int(input())
    for i in range(m):
        next_line = input()
        coeff_and_exp = next_line.split(" ")
        p.insert_term(coeff_and_exp[0], coeff_and_exp[1])
    sum_lists = p.add(q)
    print(sum_lists)
    product = p.mult(q)
    print(product)



if __name__ == "__main__":
    main()