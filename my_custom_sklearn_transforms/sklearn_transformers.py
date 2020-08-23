from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')

# All sklearn Transforms must have the `transform` and `fit` methods
class process_data(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        df = X.copy()
        # remove NA where PERFIL = HUMANAS. (strange correspondency)
        df.drop(df[(df.NOTA_GO.isnull()) & (df.PERFIL == 'HUMANAS')].index, inplace=True)

        # some values are out of range. Changing to max allowed value.
        cols = ["NOTA_MF"]
        df_data_1.loc[df_data_1.NOTA_MF >10, cols] = 10

        # remove missclassified lines
        temp = []
        trigger = 6.7
        for index,line in df.iterrows():
            i = index
            temp.append([index])
            #print(index)
            if (line.NOTA_DE < trigger) or (line.REPROVACOES_DE > 0):
                temp[-1].append("DE")
            if (line.NOTA_EM < trigger) or (line.REPROVACOES_EM > 0):
                temp[-1].append("EM")
            if (line.NOTA_MF < trigger) or (line.REPROVACOES_MF > 0):
                temp[-1].append("MF")
            if (line.NOTA_GO < trigger) or (line.REPROVACOES_GO > 0):
                temp[-1].append("GO")
            if len(temp[-1]) > 2 :
                if line.PERFIL != "DIFICULDADE":
                    df.at[i,"PERFIL"] = "REMOVE"        
            elif (len(temp[-1]) == 2):
                if (temp[-1][-1] == "DE") or (temp[-1][-1] == "EM") or (temp[-1][-1] == "GO"):
                    if line.PERFIL != "HUMANAS":
                        df.at[i,"PERFIL"] = "REMOVE"
                elif (temp[-1][-1] == "MF"):
                    if line.PERFIL != "EXATAS":
                        df.at[i,"PERFIL"] = "REMOVE"
            elif (len(temp[-1]) == 1):  # MUITO_BOM E EXCELENTE                
                m = [line.NOTA_DE, line.NOTA_EM, line.NOTA_EM, line.NOTA_GO]
                #print(m)
                count = 0
                soma = 0
                a = np.NaN
                for e in m:
                    if ((e != 0) and (not(math.isnan(e)))):
                        soma += e
                        count += 1                
                if count > 0:
                    mean = soma/count
                #print(mean)
                if (mean >= 8) and (line.PERFIL !="EXCELENTE"):
                   # df.at[i,"PERFIL"] = "REMOVER"
                    pass
                elif ((mean >= 7 ) and (mean < 8) and (line.PERFIL !="MUITO_BOM")):
                  #  df.at[i,"PERFIL"] = "REMOVER"
                    pass
            #print(temp)

        df.drop(df[(df.PERFIL == "REMOVE")].index,inplace=True)
        df.drop(df[(df.PERFIL == "REMOVER")].index,inplace=True)

        # Retornamos um novo dataframe com as modificações desejadas
        return df

class process_data2(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        df = X.copy()
        # remove NA where PERFIL = HUMANAS. (strange correspondency)
        df.drop(df[(df.NOTA_GO.isnull()) & (df.PERFIL == 'HUMANAS')].index, inplace=True)

        # some values are out of range. Changing to max allowed value.
        cols = ["NOTA_MF"]
        df_data_1.loc[df_data_1.NOTA_MF >10, cols] = 10

        # remove missclassified lines
        temp = []
        trigger = 6.7
        for index,line in df.iterrows():
            i = index
            temp.append([index])
            #print(index)
            if (line.NOTA_DE < trigger) or (line.REPROVACOES_DE > 0):
                temp[-1].append("DE")
            if (line.NOTA_EM < trigger) or (line.REPROVACOES_EM > 0):
                temp[-1].append("EM")
            if (line.NOTA_MF < trigger) or (line.REPROVACOES_MF > 0):
                temp[-1].append("MF")
            if (line.NOTA_GO < trigger) or (line.REPROVACOES_GO > 0):
                temp[-1].append("GO")
            if len(temp[-1]) > 2 :
                if line.PERFIL != "DIFICULDADE":
                    df.at[i,"PERFIL"] = "REMOVE"        
            elif (len(temp[-1]) == 2):
                if (temp[-1][-1] == "DE") or (temp[-1][-1] == "EM") or (temp[-1][-1] == "GO"):
                    if line.PERFIL != "HUMANAS":
                        df.at[i,"PERFIL"] = "REMOVE"
                elif (temp[-1][-1] == "MF"):
                    if line.PERFIL != "EXATAS":
                        df.at[i,"PERFIL"] = "REMOVE"
            elif (len(temp[-1]) == 1):  # MUITO_BOM E EXCELENTE                
                m = [line.NOTA_DE, line.NOTA_EM, line.NOTA_EM, line.NOTA_GO]
                #print(m)
                count = 0
                soma = 0
                a = np.NaN
                for e in m:
                    if ((e != 0) and (not(math.isnan(e)))):
                        soma += e
                        count += 1                
                if count > 0:
                    mean = soma/count
                #print(mean)
                if (mean >= 8) and (line.PERFIL !="EXCELENTE"):
                    df.at[i,"PERFIL"] = "REMOVER"
                    pass
                elif ((mean >= 7 ) and (mean < 8) and (line.PERFIL !="MUITO_BOM")):
                    df.at[i,"PERFIL"] = "REMOVER"
                    pass
            #print(temp)

        df.drop(df[(df.PERFIL == "REMOVE")].index,inplace=True)
        df.drop(df[(df.PERFIL == "REMOVER")].index,inplace=True)

        # Retornamos um novo dataframe com as modificações desejadas
        return df
