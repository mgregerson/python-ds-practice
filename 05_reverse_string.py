def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """

    letters = list(phrase)
    letters.reverse()
    reversed = ''
    for letter in letters:
        reversed += letter

    return phrase[::-1]