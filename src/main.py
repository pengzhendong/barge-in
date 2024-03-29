# Copyright (c) 2024, Zhendong Peng (pzd17@tsinghua.org.cn)
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
# limitations under the License.

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return True


@app.get("/check")
def check(text: str = ""):
    text = text.replace("。", "")
    digits = "零幺一二三四五六七八九"
    spokens = "嗯哦呃噢啊唉"
    concerts = "好的是对行"
    allowed_chars = digits + spokens + concerts
    res = not all(char in allowed_chars for char in text) and len(text) > 2
    return {"break": res}
