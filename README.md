# API de Recrutamento
Api utilizada nas soluções do Recruta Arpex e dinâmicas do RC

### `GET` - Busca candidato
`{{host}}/recruitment/<EVENTO>/find/<EMAIL_DO_CANDIDATO>`
> Busca dados de um determinado candiadato por evento

+ Response
``` json
{
  "success": true,
  "user": {
    "college": "UFT - Universidade Federal de Tatooine",
    "cultural_fit": "Alto",
    "email": "askywalker@tatooine.com.br",
    "event": "recruta_12_08",
    "graduation": "Academia Jedi",
    "is_present": true,
    "logic_test": 83.18,
    "mobile_phone": "XXXXXXXXXXX",
    "name": "Anakin Skywalker"
  }
}
```

### `POST` - Atualiza a presença
`{{host}}/recruitment/<EVENTO>/find/<EMAIL_DO_CANDIDATO>`
> Atualiza a presença do candidato no evento, para criação dos grupos

* Request
```json
{
  "email":"lucashippertt@id.uff.br",
  "is_present": false
}
```

+ Response
``` json
{
  "success": true
}
```

### LICENSE
```
MIT License

Copyright (c) 2017 Stone Pagamentos

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```
