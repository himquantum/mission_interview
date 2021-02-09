
# def generate_json(app_host, row_title, output_json_file):
def generate_json():
    import json
    sample_json = 'C:\\Users\\hikumar\\Downloads\\grafana OMS\\test\\OMS_ICM12.json'
    '''
    The sample JSON file contains only Grafana row json.
    The head and tail of full Grafana will be added later
    '''
    queries = []
    with open(sample_json) as jfile:
        parsed = json.load(jfile)
        #print(parsed.panels[0].panels[0].targets[0].query)
        for pan in parsed["panels"]:
            for each in pan["panels"][0]:
                print(each[])


generate_json()