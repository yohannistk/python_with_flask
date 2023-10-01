
from flask import Flask, request, jsonify
from diffusers import DiffusionPipeline
import torch
app = Flask(__name__)

@app.route('/process_string', methods=['GET'])
def process_string():
    string_param = request.args.get('string')
    
    if string_param:
        # Process the string here
        pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
        # pipe.to("cuda")

        # if using torch < 2.0
        # pipe.enable_xformers_memory_efficient_attention()

        images = pipe(prompt=string_param)
        # processed_string = string_param.upper()  # Example: convert to uppercase
        return f"Processed string: {jsonify(images)}"
    else:
        return "No string parameter provided!!!."

if __name__ == '__main__':
    app.run()
