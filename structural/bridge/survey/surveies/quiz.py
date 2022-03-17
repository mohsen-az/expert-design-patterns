from structural.bridge.survey.contracts.survey import Survey


class QuizSurvey(Survey):

    def __init__(self, presentation):
        super().__init__(presentation)

    def display(self):
        return self.presentation.present()
