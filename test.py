from paddlex import create_model
model = create_model('PP-Chart2Table')
results = model.predict(
    input={"image": "/home/zeinabrm/Documents/ChartToText/Project/ChartAnalyzer/multiset_barchart.png"},
    batch_size=1
)
for res in results:
    res.print()
    res.save_to_json(f"./output/res.json")



# Available models: models=[Model(model='qwen2.5:latest', modified_at=datetime.datetime(2025, 4, 20, 17, 56, 38, 480761, tzinfo=TzInfo(UTC)), digest='845dbda0ea48ed749caafd9e6037047aa19acfcfd82e704d7ca97d631a0b697e', size=4683087332, details=ModelDetails(parent_model='', format='gguf', family='qwen2', families=['qwen2'], parameter_size='7.6B', quantization_level='Q4_K_M'))
#                           , Model(model='almaghrabima/ALLaM-Thinking:latest', modified_at=datetime.datetime(2025, 3, 20, 19, 42, 49, 644450, tzinfo=TzInfo(UTC)), digest='dd366456e63970b19d414a5fcf6e210d25d3e754eb797aac1e8850885e93f365', size=4263195351, details=ModelDetails(parent_model='', format='gguf', family='llama', families=['llama'], parameter_size='7.0B', quantization_level='Q4_K_M')),
#                             Model(model='gemma3:27b', modified_at=datetime.datetime(2025, 3, 12, 12, 33, 20, 925514, tzinfo=TzInfo(UTC)), digest='30ddded7fba6d6f9c2f26661e2feba2d7a26a75e20a817538c41c3716d92609d', size=17396936887, details=ModelDetails(parent_model='', format='gguf', family='gemma3', families=['gemma3'], parameter_size='27.4B', quantization_level='Q4_K_M')), 
#                             Model(model='command-r7b-arabic:latest', modified_at=datetime.datetime(2025, 3, 12, 7, 29, 8, 634445, tzinfo=TzInfo(UTC)), digest='4bbe3353e56a7bad7512de135cf875f8cd31b10cd2310c257ce5d4f98a43fe9e', size=5057031326, details=ModelDetails(parent_model='', format='gguf', family='cohere2', families=['cohere2'], parameter_size='8.0B', quantization_level='Q4_K_M')), 
#                             Model(model='llava:34b', modified_at=datetime.datetime(2025, 2, 12, 13, 32, 11, 449775, tzinfo=TzInfo(UTC)), digest='3d2d24f4667475bd28d515495b0dcc03b5a951be261a0babdb82087fc11620ee', size=20166497526, details=ModelDetails(parent_model='', format='gguf', family='llama', families=['llama', 'clip'], parameter_size='34B', quantization_level='Q4_0')), 
#                             Model(model='codestral:latest', modified_at=datetime.datetime(2025, 2, 4, 15, 23, 15, 358294, tzinfo=TzInfo(UTC)), digest='0898a8b286d56d8105587049fec69634fce83c957230fc13f0acfe03b7b11909', size=12569170438, details=ModelDetails(parent_model='', format='gguf', family='llama', families=['llama'], parameter_size='22.2B', quantization_level='Q4_0')), 
#                             Model(model='qwen2.5-coder:32b', modified_at=datetime.datetime(2025, 2, 4, 8, 57, 6, 569891, tzinfo=TzInfo(UTC)), digest='4bd6cbf2d094264457a17aab6bd6acd1ed7a72fb8f8be3cfb193f63c78dd56df', size=19851349856, details=ModelDetails(parent_model='', format='gguf', family='qwen2', families=['qwen2'], parameter_size='32.8B', quantization_level='Q4_K_M')), 
#                             Model(model='mistral-small:latest', modified_at=datetime.datetime(2025, 2, 3, 16, 24, 20, 151181, tzinfo=TzInfo(UTC)), digest='8039dd90c1138d772437a0779a33b7349efd5d9cca71edcd26e4dd463f90439d', size=14333921662, details=ModelDetails(parent_model='', format='gguf', family='llama', families=['llama'], parameter_size='23.6B', quantization_level='Q4_K_M')), 
#                             Model(model='deepseek-r1:14b', modified_at=datetime.datetime(2025, 2, 3, 8, 46, 0, 433369, tzinfo=TzInfo(UTC)), digest='ea35dfe18182f635ee2b214ea30b7520fe1ada68da018f8b395b444b662d4f1a', size=8988112040, details=ModelDetails(parent_model='', format='gguf', family='qwen2', families=['qwen2'], parameter_size='14.8B', quantization_level='Q4_K_M'))]
# 