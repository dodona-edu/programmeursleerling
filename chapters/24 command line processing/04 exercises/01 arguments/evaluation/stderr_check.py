from evaluation_utils import EvaluationResult

MESSAGES = {
    'en': 'sum: invalid arguments',
    'nl': 'som: ongeldige argumenten',
}


def evaluate(context):
    expected = MESSAGES.get(context.natural_language, MESSAGES['en'])
    actual = (context.actual or '').strip()
    return EvaluationResult(actual == expected, expected, actual)
