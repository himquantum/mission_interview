def generate_json(app_host, row_title, output_json_file):
    import json
    sample_json = 'C:\\Users\\hikumar\\Downloads\\grafana OMS\\test\\Grafana_row_sample.json'
    row_gap = 6
    '''
    The sample JSON file contains only Grafana row json.
    The head and tail of full Grafana will be added later
    '''
    queries = []
    with open(sample_json) as jfile:
        parsed = json.load(jfile)
        parsed["gridPos"]["y"] += row_gap
        parsed["title"] = row_title

        for panel in parsed["panels"]:
            panel["gridPos"]["y"] += row_gap
            query = str(panel["targets"][0]["query"])
            # update queries as per app_name
            query = query.replace("var_app_host", app_host)
            panel["targets"][0]["query"] = query

    row_gap += 6
    # print(parsed["gridPos"])
    # print(parsed["panels"][0]["gridPos"])

    with open(output_json_file, 'a+') as write_file:
        json.dump(parsed, write_file, indent=1)
        print("\n,", file=write_file)


app_list = [
    ["OrderCreateWeb-NA-Azeus-Prod", "OrderCreate"],
    ["OrderValidateWeb-NA-Azeus-Prod", "OrderValidate"],
    ["OrderVerifyWeb-NA-Azeus-Prod", "OrderVerify"],
    ["OrderSourceWeb-NA-Azeus-Prod", "OrderSource"],
    ["OrderReleaseWeb-NA-Azeus-Prod", "OrderRelease"],
    ["BOLProcessorProvider-NA-Azeus-Prod", "BOLProcessorProvider"],
    ["FinancialsWeb-NA-Azeus-Prod", "Financials"],
    ["OrderModifyServiceProvider-NA-Azeus-Prod", "OrderModifyServiceProvider"],
    ["OrderConfigurationWeb-NA-Azeus-Prod", "OrderConfiguration"],
    ["OrderCancelWeb-NA-Azeus-Prod", "OrderCancel"],
    ["OrderCompleteWeb-NA-Azeus-Prod", "OrderComplete"],
    ["RESTOrderStatusServiceProvider-NA-Azeus-Prod", "RESTOrderStatusServiceProvider"]
]

for app_host1, row_title1 in app_list:
    generate_json(app_host1, row_title1, "output_json_file1.json")
