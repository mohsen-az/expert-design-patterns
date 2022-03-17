from behavioral.template_method.reporter.contracts.report import UserReport


class ReportInHTML(UserReport):

    def export(self):
        """
        Export data in HTML Format
        :return:
        """
        data = self.data_to_export
        print(f"Export Report In HTML Format")