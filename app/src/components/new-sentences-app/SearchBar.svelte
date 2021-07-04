<script lang="ts">
  import { Search, Button, ButtonSet } from "carbon-components-svelte";
  import type { JibikiSenteceResponse, SentecePart } from "src/models/Jibiki";
  import SentenceSourceSelect from "../SentenceSourceSelect.svelte";
  import { Index, Document } from "flexsearch";
  import { onMount } from "svelte";

  export let sentences: JibikiSenteceResponse[];

  let loading = false;
  let searchValue = "";

  const docs = [
    {
      Source: "jlpt-tango/n3",
      Sentence:
        "＜Ａ＞画面表記での使用になんらかの『ルール』(口頭での指示や了解事項を含む)を設けていますか？",
      Translation:
        "A: Whish do you most resemble, your mother or your father? B: I'm told I resemble my father.",
      Words: [
        "画面",
        "表記",
        "使用に",
        "なんらかの",
        "ルール",
        "口頭",
        "指示",
        "了解",
        "事項",
        "含む",
        "設けています",
      ],
      WordPositions: [
        {
          Start: 3,
          End: 5,
        },
        {
          Start: 5,
          End: 7,
        },
        {
          Start: 9,
          End: 12,
        },
        {
          Start: 12,
          End: 17,
        },
        {
          Start: 18,
          End: 21,
        },
        {
          Start: 23,
          End: 25,
        },
        {
          Start: 27,
          End: 29,
        },
        {
          Start: 30,
          End: 32,
        },
        {
          Start: 32,
          End: 34,
        },
        {
          Start: 35,
          End: 37,
        },
        {
          Start: 39,
          End: 45,
        },
      ],
      Lemmas: [
        "画面",
        "表記",
        "使用",
        "なんらかの",
        "ルール",
        "口頭",
        "指示",
        "了解",
        "事項",
        "含む",
        "設ける",
      ],
      Readings: [
        "ガメン",
        "ヒョウキ",
        "シヨウニ",
        "ナンラカノ",
        "ルール",
        "コウトウ",
        "シジ",
        "リョウカイ",
        "ジコウ",
        "フクム",
        "モウケテイマス",
      ],
    },
    {
      Source: "jlpt-tango/n3",
      Sentence:
        "　⇒たとえば、「使用はスポーツ系番組やスポーツニュースに限る」「一般の報道ニュースでは乱用しない」「見出し、メインタイトル、サイドタイトルに限る」など。",
      Translation:
        "A: Whish do you most resemble, your mother or your father? B: I'm told I resemble my father.",
      Words: [
        "たとえば",
        "使用",
        "スポーツ系",
        "番組",
        "スポーツ",
        "ニュースに",
        "限る",
        "一般",
        "報道",
        "ニュース",
        "乱用",
        "しない",
        "見出し",
        "メイン",
        "タイトル",
        "サイド",
        "タイトルに",
        "限る",
      ],
      WordPositions: [
        {
          Start: 2,
          End: 6,
        },
        {
          Start: 8,
          End: 10,
        },
        {
          Start: 11,
          End: 16,
        },
        {
          Start: 16,
          End: 18,
        },
        {
          Start: 19,
          End: 23,
        },
        {
          Start: 23,
          End: 28,
        },
        {
          Start: 28,
          End: 30,
        },
        {
          Start: 32,
          End: 34,
        },
        {
          Start: 35,
          End: 37,
        },
        {
          Start: 37,
          End: 41,
        },
        {
          Start: 43,
          End: 45,
        },
        {
          Start: 45,
          End: 48,
        },
        {
          Start: 50,
          End: 53,
        },
        {
          Start: 54,
          End: 57,
        },
        {
          Start: 57,
          End: 61,
        },
        {
          Start: 62,
          End: 65,
        },
        {
          Start: 65,
          End: 70,
        },
        {
          Start: 70,
          End: 72,
        },
      ],
      Lemmas: [
        "たとえば",
        "使用",
        "スポーツ系",
        "番組",
        "スポーツ",
        "ニュース",
        "限る",
        "一般",
        "報道",
        "ニュース",
        "乱用",
        "する",
        "見出し",
        "メイン",
        "タイトル",
        "サイド",
        "タイトル",
        "限る",
      ],
      Readings: [
        "タトエバ",
        "シヨウ",
        "スポーツケイ",
        "バングミ",
        "スポーツ",
        "ニュースニ",
        "カギル",
        "イッパン",
        "ホウドウ",
        "ニュース",
        "ランヨウ",
        "シナイ",
        "ミダシ",
        "メイン",
        "タイトル",
        "サイド",
        "タイトルニ",
        "カギル",
      ],
    },
    {
      Source: "jlpt-tango/n3",
      Sentence: "＜Ｂ＞『表記』はどうしていますか？",
      Translation:
        "A: Whish do you most resemble, your mother or your father? B: I'm told I resemble my father.",
      Words: ["表記", "どう", "しています"],
      WordPositions: [
        {
          Start: 4,
          End: 6,
        },
        {
          Start: 8,
          End: 10,
        },
        {
          Start: 10,
          End: 15,
        },
      ],
      Lemmas: ["表記", "どう", "する"],
      Readings: ["ヒョウキ", "ドウ", "シテイマス"],
    },
    {
      Source: "jlpt-tango/n3",
      Sentence:
        "　⇒「vs.」は本来小文字で「省略符（ピリオド）」が必要ですが、「大文字(前後の文字と同じ大きさということ)でも可」としていますか。",
      Translation:
        "A: Whish do you most resemble, your mother or your father? B: I'm told I resemble my father.",
      Words: [
        "本来",
        "小文字",
        "省略",
        "符",
        "ピリオド",
        "必要",
        "です",
        "大文字",
        "前後",
        "文字",
        "同じ",
        "大きさ",
        "こと",
        "可",
        "しています",
      ],
      WordPositions: [
        {
          Start: 8,
          End: 10,
        },
        {
          Start: 10,
          End: 13,
        },
        {
          Start: 15,
          End: 17,
        },
        {
          Start: 17,
          End: 18,
        },
        {
          Start: 19,
          End: 23,
        },
        {
          Start: 26,
          End: 28,
        },
        {
          Start: 28,
          End: 30,
        },
        {
          Start: 33,
          End: 36,
        },
        {
          Start: 37,
          End: 39,
        },
        {
          Start: 40,
          End: 42,
        },
        {
          Start: 43,
          End: 45,
        },
        {
          Start: 45,
          End: 48,
        },
        {
          Start: 51,
          End: 53,
        },
        {
          Start: 56,
          End: 57,
        },
        {
          Start: 59,
          End: 64,
        },
      ],
      Lemmas: [
        "本来",
        "小文字",
        "省略",
        "符",
        "ピリオド",
        "必要",
        "です",
        "大文字",
        "前後",
        "文字",
        "同じ",
        "大きい",
        "こと",
        "可",
        "する",
      ],
      Readings: [
        "ホンライ",
        "コモジ",
        "ショウリャク",
        "フ",
        "ピリオド",
        "ヒツヨウ",
        "デス",
        "ダイモンジ",
        "ゼンゴ",
        "モジ",
        "オナジ",
        "オオキサ",
        "コト",
        "カ",
        "シテイマス",
      ],
    },
    {
      Source: "jlpt-tango/n3",
      Sentence: "「省略符は不要ですか必要ですか」。",
      Translation:
        "A: Whish do you most resemble, your mother or your father? B: I'm told I resemble my father.",
      Words: ["省略", "符", "不要", "です", "必要", "です"],
      WordPositions: [
        {
          Start: 1,
          End: 3,
        },
        {
          Start: 3,
          End: 4,
        },
        {
          Start: 5,
          End: 7,
        },
        {
          Start: 7,
          End: 9,
        },
        {
          Start: 10,
          End: 12,
        },
        {
          Start: 12,
          End: 14,
        },
      ],
      Lemmas: ["省略", "符", "不要", "です", "必要", "です"],
      Readings: ["ショウリャク", "フ", "フヨウ", "デス", "ヒツヨウ", "デス"],
    },
    {
      Source: "jlpt-tango/n3",
      Sentence: "＜Ｃ＞『読み』はどうしていますか？",
      Translation:
        "A: Whish do you most resemble, your mother or your father? B: I'm told I resemble my father.",
      Words: ["読み", "どう", "しています"],
      WordPositions: [
        {
          Start: 4,
          End: 6,
        },
        {
          Start: 8,
          End: 10,
        },
        {
          Start: 10,
          End: 15,
        },
      ],
      Lemmas: ["読み", "どう", "する"],
      Readings: ["ヨミ", "ドウ", "シテイマス"],
    },
    {
      Source: "jlpt-tango/n3",
      Sentence:
        "　⇒英語の発音はバーサス(versus　ヴァーサス)ですが、この読み方は聞いたことがありません。",
      Translation:
        "A: Whish do you most resemble, your mother or your father? B: I'm told I resemble my father.",
      Words: [
        "英語",
        "発音",
        "です",
        "この",
        "読み方",
        "聞いた",
        "こと",
        "ありません",
      ],
      WordPositions: [
        {
          Start: 2,
          End: 4,
        },
        {
          Start: 5,
          End: 7,
        },
        {
          Start: 26,
          End: 28,
        },
        {
          Start: 30,
          End: 32,
        },
        {
          Start: 32,
          End: 35,
        },
        {
          Start: 36,
          End: 39,
        },
        {
          Start: 39,
          End: 41,
        },
        {
          Start: 42,
          End: 47,
        },
      ],
      Lemmas: [
        "英語",
        "発音",
        "です",
        "この",
        "読み方",
        "聞く",
        "こと",
        "ある",
      ],
      Readings: [
        "エイゴ",
        "ハツオン",
        "デス",
        "コノ",
        "ヨミカタ",
        "キイタ",
        "コト",
        "アリマセン",
      ],
    },
    {
      Source: "jlpt-tango/n3",
      Sentence: 'ふつうは「○○"対"××」と読むでしょう。',
      Translation:
        "A: Whish do you most resemble, your mother or your father? B: I'm told I resemble my father.",
      Words: ["ふつう", "対", "読む", "でしょ"],
      WordPositions: [
        {
          Start: 0,
          End: 3,
        },
        {
          Start: 8,
          End: 9,
        },
        {
          Start: 14,
          End: 16,
        },
        {
          Start: 16,
          End: 19,
        },
      ],
      Lemmas: ["ふつう", "対", "読む", "です"],
      Readings: ["フツウ", "タイ", "ヨム", "デショ"],
    },
    {
      Source: "jlpt-tango/n3",
      Sentence: "ブイエス(ヴイエス)と読むこともありますか。",
      Translation:
        "A: Whish do you most resemble, your mother or your father? B: I'm told I resemble my father.",
      Words: ["読む", "こと", "あります"],
      WordPositions: [
        {
          Start: 11,
          End: 13,
        },
        {
          Start: 13,
          End: 15,
        },
        {
          Start: 16,
          End: 20,
        },
      ],
      Lemmas: ["読む", "こと", "ある"],
      Readings: ["ヨム", "コト", "アリマス"],
    },
    {
      Source: "jlpt-tango/n3",
      Sentence:
        "局のアナウンサーだけでなく、外部のリポーターやナレーターにどのように読ませているでしょうか。",
      Translation:
        "A: Whish do you most resemble, your mother or your father? B: I'm told I resemble my father.",
      Words: [
        "局",
        "アナウンサー",
        "でなく",
        "外部",
        "リポーター",
        "ナレーターに",
        "どの",
        "ように",
        "読ませている",
        "でしょ",
      ],
      WordPositions: [
        {
          Start: 0,
          End: 1,
        },
        {
          Start: 2,
          End: 8,
        },
        {
          Start: 10,
          End: 13,
        },
        {
          Start: 14,
          End: 16,
        },
        {
          Start: 17,
          End: 22,
        },
        {
          Start: 23,
          End: 29,
        },
        {
          Start: 29,
          End: 31,
        },
        {
          Start: 31,
          End: 34,
        },
        {
          Start: 34,
          End: 40,
        },
        {
          Start: 40,
          End: 43,
        },
      ],
      Lemmas: [
        "局",
        "アナウンサー",
        "だ",
        "外部",
        "リポーター",
        "ナレーター",
        "どの",
        "よう",
        "読む",
        "です",
      ],
      Readings: [
        "ツボネ",
        "アナウンサー",
        "デナク",
        "ガイブ",
        "リポーター",
        "ナレーターニ",
        "ドノ",
        "ヨウニ",
        "ヨマセテイル",
        "デショ",
      ],
    },
    {
      Source: "jlpt-tango/n3",
      Sentence: "テレビ朝日の報道では、表記も読みもルールはない。",
      Translation:
        "A: Whish do you most resemble, your mother or your father? B: I'm told I resemble my father.",
      Words: ["テレビ朝日", "報道", "表記", "読み", "ルール"],
      WordPositions: [
        {
          Start: 0,
          End: 5,
        },
        {
          Start: 6,
          End: 8,
        },
        {
          Start: 11,
          End: 13,
        },
        {
          Start: 14,
          End: 16,
        },
        {
          Start: 17,
          End: 20,
        },
      ],
      Lemmas: ["テレビ朝日", "報道", "表記", "読む", "ルール"],
      Readings: ["テレビアサヒ", "ホウドウ", "ヒョウキ", "ヨミ", "ルール"],
    },
    {
      Source: "jlpt-tango/n3",
      Sentence:
        "ただ、最近よく出て来るものの、そもそも「vs.」は「日本語ではない」（外来語でもない）と思うのだが・・・・。",
      Translation:
        "A: Whish do you most resemble, your mother or your father? B: I'm told I resemble my father.",
      Words: [
        "ただ",
        "最近",
        "よく",
        "出て来る",
        "そもそも",
        "日本語",
        "ない",
        "外来語",
        "ない",
        "思う",
        "の",
        "だ",
      ],
      WordPositions: [
        {
          Start: 0,
          End: 2,
        },
        {
          Start: 3,
          End: 5,
        },
        {
          Start: 5,
          End: 7,
        },
        {
          Start: 7,
          End: 11,
        },
        {
          Start: 15,
          End: 19,
        },
        {
          Start: 26,
          End: 29,
        },
        {
          Start: 31,
          End: 33,
        },
        {
          Start: 35,
          End: 38,
        },
        {
          Start: 40,
          End: 42,
        },
        {
          Start: 44,
          End: 46,
        },
        {
          Start: 46,
          End: 47,
        },
        {
          Start: 47,
          End: 48,
        },
      ],
      Lemmas: [
        "ただ",
        "最近",
        "よく",
        "出る",
        "そもそも",
        "日本語",
        "ない",
        "外来語",
        "ない",
        "思う",
        "の",
        "だ",
      ],
      Readings: [
        "タダ",
        "サイキン",
        "ヨク",
        "デテクル",
        "ソモソモ",
        "ニホンゴ",
        "ナイ",
        "ガイライゴ",
        "ナイ",
        "オモウ",
        "ノ",
        "ダ",
      ],
    },
  ];

  const index = new Document({
    document: {
      index: ["Words", "Lemmas", "Readings"],
      store: ["Sentence", "Words", "Lemmas", "WordPositions"],
    },
  });

  onMount(() => {
    docs.forEach((doc, i) => index.add({ id: i, ...doc }));
  });

  function insertAtIndex(s: string, insertString: string, index: number) {
    return s.substring(0, index) + insertString + s.substring(index);
  }

  function getHighloteSentenceParts(
    s: Solr.Doc,
    searchWord: string
  ): SentecePart[] {
    let foundIndex = s.Words.indexOf(searchWord);
    if (foundIndex === -1) {
      foundIndex = s.Lemmas.indexOf(searchWord);
    }
    if (foundIndex === -1) {
      return [
        {
          part: s.Sentence,
          highlight: false,
        },
      ];
    }

    const wordPosition = s.WordPositions[foundIndex];

    let sentenceParts: SentecePart[] = [];
    sentenceParts.push({
      part: s.Sentence.substring(0, wordPosition.Start),
      highlight: false,
    });
    sentenceParts.push({
      part: s.Sentence.substring(wordPosition.Start, wordPosition.End),
      highlight: true,
    });
    sentenceParts.push({
      part: s.Sentence.substring(wordPosition.End),
      highlight: false,
    });

    return sentenceParts;
  }

  async function fetchSentences() {
    const result = index.search(searchValue, {
      enrich: true,
    }) as FlexSearch.RootObject[];

    console.log(JSON.stringify(result));

    const b = new Set<Solr.Doc>(
      result.flatMap((a) => a.result.map((r) => r.doc))
    );
    const a = Array.from(b.values());

    sentences = a.map((s, i) => ({
      id: i,
      sentence: s.Sentence,
      sentenceParts: getHighloteSentenceParts(s, searchValue),
      tags: ["A", "B"],
      language: "JA",
      translations: [],
    }));

    // const searchQuery = encodeURIComponent(
    //   `Words:${searchValue} OR Lemmas:${searchValue}`
    // );
    // const url = `http://localhost:7070/search/kanji/select?q=${searchQuery}`;

    // loading = true;
    // fetch(url)
    //   .then((r) => r.json())
    //   .then(
    //     (r: Solr.SolrSearchResponse) =>
    //       (sentences = r.response.docs.map((s, i) => ({
    //         id: i,
    //         language: "a",
    //         sentence: s.Sentence,
    //         tags: ["A", "B"],
    //         translations: [
    //           {
    //             id: 13,
    //             language: "ENG",
    //             sentence: "This is a Translation",
    //           },
    //         ],
    //       })))
    //   )
    //   .catch((e) => console.log(e))
    //   .finally(() => (loading = false));
  }
</script>

<ButtonSet style={"width:100%"}>
  <Search
    bind:value={searchValue}
    on:input={fetchSentences}
    placeholder="Enter a phrase..."
  />
  <SentenceSourceSelect />
  <Button skeleton={loading} on:click={fetchSentences}>Search</Button>
</ButtonSet>
