class Fabric:
    name_type = None
    extracted_resources: {} # data = extracted_resources[res].
    # data["type"] - в процентах от остатка или численно ресурсы
    # data["quantity"] - число (единиц или процентов)

    def __init__(self, name):
        self.name = name

    def extract(self, name_res, explorer_res) -> float|int:
        if name_res not in explorer_res:
            return 0

        data = self.extracted_resources[name_res]
        if data["type"] == "interest":
            return explorer_res * data["quantity"]

        return data["quantity"]