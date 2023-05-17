# Copyright The Caikit Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License

# Third Party
import gradio as gr
import grpc


class Conversational:
    def __init__(self, request, predict) -> None:
        self.request = request
        self.predict = predict

    def fn(self, model, text_in, chat):
        if text_in:
            response = self.predict(
                self.request(text_in=text_in), metadata=[("mm-model-id", model)]
            ).text
            chat.append((text_in, response))
        return "", chat  # '' is to clear inputs

    @classmethod
    def optional_tab(cls, models, request, predict):
        if not models:
            return False

        tab = cls.__name__  # tab name
        try:
            this = cls(request, predict)
            with gr.Tab(tab):
                model_choice = gr.Dropdown(
                    label="Model ID", choices=models, value=models[0]
                )
                outputs = gr.Chatbot()
                inputs = gr.Textbox(
                    label="Input Text (hit enter to send)",
                    placeholder=f"Enter input text for {tab}",
                )
                inputs.submit(
                    this.fn,
                    [model_choice, inputs, outputs],
                    [inputs, outputs],
                    api_name=tab,
                )

                clear = gr.Button("Clear")
                clear.click(lambda: None, None, outputs, queue=False)

                print(f"✅️  {tab} tab is enabled!")
                return True
        except grpc.RpcError as rpc_error:
            print(f"⚠️  Disabling {tab} tab due to:  {rpc_error.details()}")
            return False
