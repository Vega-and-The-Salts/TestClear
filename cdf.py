
class ConstructDataFrame:
    def __init__(self, df):
        self.df = df

    def remove_spaces(self):
        self.df = self.df.columns.replace('\n', ' ', regex = True)

    def add_column_percents(self):
        self.df['% EN'] = self.df['Total'] / self.df['Total FC']
        self.df['% EN'] = self.df['% EN'].round(decimals= 2)

    def group_indexing(self):
        self.df = self.df.set_index(['GR #', 'GR Name'])