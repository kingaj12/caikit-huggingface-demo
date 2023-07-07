# Makefile to generate Docker images for runtime and clients

.PHONY: caikit gradio clean

# gradio build
GRADIO_DOCKER_DIR   	:= ./docker/gradio
GRADIO_DOCKERFILE	:= $(GRADIO_DOCKER_DIR)/Dockerfile
GRADIO_FILES 		:= gradio_client models module_ids.py 

gradio: $(GRADIO_FILES) $(GRADIO_DOCKERFILE)
	cp -r $(GRADIO_FILES) $(GRADIO_DOCKER_DIR) 

clean: 
	cd $(GRADIO_DOCKER_DIR) && rm -rf $(GRADIO_FILES) 



