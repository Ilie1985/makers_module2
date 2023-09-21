
class GrammarStats:
    def __init__(self):
        self.total_texts = 0
        self.passed_texts = 0

    def check(self, text):
        # Increment the total_texts counter
        self.total_texts += 1

        # Check if the text begins with a capital letter and ends with a punctuation mark
        if text and text[0].isupper() and text[-1] in ['.', '!', '?']:
            # Increment the passed_texts counter if the check passes
            self.passed_texts += 1
            return True
        else:
            return False

    def percentage_good(self):
        # Calculate the percentage of texts that passed the check
        if self.total_texts == 0:
            return 0
        return (self.passed_texts / self.total_texts) * 100

