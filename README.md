# LLAMA-LLM-API

A short program to get started on the LLAMA LLM on the local system.

# Llama Model Installation Guide

## Table of Contents
- Tiny Models Comparison
- Installation Steps
- Hardware Recommendations
- Running Models with Ollama

## Tiny Models Comparison

| Model Name                           | Size (INT4) | Context | Key Strengths                              | Best For                              |
|--------------------------------------|------------|---------|--------------------------------------------|---------------------------------------|
| Llama3.2-1B                          | ~0.5GB     | 128K    | Lightweight, general-purpose               | Basic text generation, prototyping   |
| Llama3.2-1B-Instruct                 | ~0.5GB     | 128K    | Instruction-tuned for tasks                | Simple chatbots, commands             |
| Llama3.2-1B-Instruct:int4-qlora-eo8  | ~0.25GB    | 8K      | QLoRA quantized, minimal RAM               | Edge devices, low-power hardware     |
| Llama3.2-1B-Instruct:int4-spinquant-eo8 | ~0.25GB | 8K      | SpinQuant optimized, fast inference        | Real-time apps, embedded systems     |
| Llama3.2-3B                          | ~1.5GB     | 128K    | Better coherence than 1B                   | Drafting, summarization              |
| Llama3.2-3B-Instruct                 | ~1.5GB     | 128K    | Fine-tuned for responses                   | Customer support, Q&A                |
| Llama3.2-3B-Instruct:int4-qlora-eo8  | ~0.75GB    | 8K      | Balanced performance/size                  | Local dev, lightweight chatbots      |
| Llama3.2-3B-Instruct:int4-spinquant-eo8 | ~0.75GB | 8K      | Optimized latency                          | High-speed inference needs           |
| Llama-Guard-3-1B:int4                | ~0.25GB    | 128K    | Safety/toxicity filtering                  | Content moderation, API filtering    |
| Llama-Guard-2-8B                     | ~2.0GB     | 4K      | Legacy safety model                        | Backward compatibility               |

### Key Insights
- Smallest Models: 0.25GB INT4-quantized 1B models (best for Raspberry Pi, phones)
- Best Performance/Size Tradeoff: Llama3.2-3B-Instruct:int4-qlora-eo8 (0.75GB, 8K context)
- Safety Focus: Llama-Guard-3-1B:int4 (0.25GB) for real-time content filtering
- Avoid Unquantized Models: Non-INT4 1B/3B models use 2-6x more space

## Hardware Recommendations

| Model Size | Minimum RAM | Example Devices                |
|------------|-------------|---------------------------------|
| 0.25GB     | 1GB         | Raspberry Pi 5, cheap VPS      |
| 0.75GB     | 2GB         | Older laptops, low-end PCs      |
| 1.5GB      | 4GB         | Mid-range PCs, cloud micro VMs  |

## Installation Steps

1. Install the Llama CLI:
   ```bash
   pip install llama-stack
    ```
For updating:
    ```bash
    pip install llama-stack -U
    ```

2. Find models list:
    ```bash
    llama model list
    ```

For older versions:
    ```bash
    llama model list --show-all
    ```

3. Select and download a model:
    ```bash
    llama model download --source meta --model-id MODEL_ID
    ```

4. Specify custom URL when prompted:
    ```bash
    https://llama4.llamameta.net/*?Policy=eyJTdGF0ZW1lbnQiOlt7InVuaXjE3NDQ3Mjk5Mjl9fX1dfQ__&Signature=Bspdw2rdIILmECgEE8ghi73MlhvaxQqa2MMz0IUVx-7fdw__&Key-Pair-Id=K15SLZ&Download-Request-ID=132272
    ```

## Running Models with Ollama

1. Install Ollama for Windows:
    ```bash
    https://ollama.com/download/windows
    ```

2. Run your model locally:
    ```bash
    ollama run MODEL
    ```

## Execute the program

```bash
Run pip install -r requirements.txt

run uvicorn main:app --reload
```