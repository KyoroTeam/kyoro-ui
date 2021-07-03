aws lambda update-function-code --function-name Kuromoji --zip-file fileb://target/kuromoji-tokenizer-1.0-SNAPSHOT.jar
aws --cli-binary-format raw-in-base64-out lambda invoke --function-name Kuromoji --payload '知人の紹介で、彼と知り合った。' response.json

aws --cli-binary-format raw-in-base64-out lambda invoke --function-name Kuromoji --payload '{ "request": "知人の紹介で、彼と知り合った。" }' response.json

aws --cli-binary-format raw-in-base64-out lambda invoke --function-name Kuromoji --payload '[{ "Sentence": "知人の紹介で、彼と知り合った。", "Source": "jlpt-tango" }]' response.json

aws --cli-binary-format raw-in-base64-out lambda invoke --function-name Kuromoji --payload '{ "request": "＜Ａ＞画面表記での使用になんらかの『ルール』(口頭での指示や了解事項を含む)を設けていますか？　 ⇒ たとえば、「使用はスポーツ系番組やスポーツニュースに限る」「一般の報道ニュースでは乱用しない」「見出し、メインタイトル、サイドタイトルに限る」など。＜Ｂ＞『表記』はどうしていますか？　 ⇒「vs.」は本来小文字で「省略符（ピリオド）」が必要ですが、「大文字(前後の文字と同じ大きさということ)でも可」としていますか。「省略符は不要ですか必要ですか」。＜Ｃ＞『読み』はどうしていますか？　 ⇒ 英語の発音はバーサス(versus 　ヴァーサス)ですが、この読み方は聞いたことがありません。ふつうは「○○\"対\"××」と読むでしょう。ブイエス(ヴイエス)と読むこともありますか。局のアナウンサーだけでなく、外部のリポーターやナレーターにどのように読ませているでしょうか。テレビ朝日の報道では、表記も読みもルールはない。ただ、最近よく出て来るものの、そもそも「vs.」は「日本語ではない」（外来語でもない）と思うのだが・・・・。" }' response.json
