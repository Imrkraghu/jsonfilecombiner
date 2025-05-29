import json
import gradio as gr

def merge_json_files(files):
    merged_data = []
    for file in files:
        try:
            with open(file.name, 'r') as f:
                data = json.load(f)
                merged_data.append(data)
        except json.JSONDecodeError:
            return "Invalid JSON format in one or more files"
    
    output_file = "merged.json"
    with open(output_file, 'w') as outfile:
        json.dump(merged_data, outfile, indent=4)
    
    return output_file

iface = gr.Interface(
    fn=merge_json_files,
    inputs=gr.File(file_types=[".json"], file_count="multiple", label="Upload JSON Files"),
    outputs=gr.File(label="Download Merged JSON"),
    title="JSON Merger",
    description="Upload multiple JSON files and merge them into one.",
    allow_flagging="never"  # Removes the flag button
)

iface.launch(share="True")