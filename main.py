import json
import jsonlines

with jsonlines.open('./data/output_anypage_10.jsonl') as reader:

   data = []

   for obj in reader:

      if obj["Topic"] != "finance":
         print("Topic Name is not Finance")
         obj["Topic"] = "finance"

      if "SearchKey" in obj:
         print("SearchKey exist in JSON data")
      else:
         print("SearchKey not exist in JSON data")
         searchkeyVal = obj["Title"]
         obj["Title"] = ""
         textKeyVal = obj["Text"]
         obj.pop('Text')
         obj['SearchKey'] = searchkeyVal
         obj['Text'] = textKeyVal

      data.append(obj)

with jsonlines.open('./data/output_anypage_10_fixed.jsonl', 'w') as writer:
   writer.write_all(data)

