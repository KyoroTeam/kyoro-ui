<script lang="ts">
  import { Search, Button, ButtonSet } from "carbon-components-svelte";
  import type { JibikiSenteceResponse } from "src/models/Jibiki";
  import SentenceSourceSelect from "../SentenceSourceSelect.svelte";
  import { Index, Document, Worker } from "flexsearch";
  import { onMount } from "svelte";

  export let sentences: JibikiSenteceResponse[];

  let loading = false;
  let searchValue = "";

  const docs = [
    {
      Sentence:
        "＜Ａ＞画面表記での使用になんらかの『ルール』(口頭での指示や了解事項を含む)を設けていますか？",
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
      Sentence:
        "　 ⇒ たとえば、「使用はスポーツ系番組やスポーツニュースに限る」「一般の報道ニュースでは乱用しない」「見出し、メインタイトル、サイドタイトルに限る」など。",
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
      Sentence: "＜Ｂ＞『表記』はどうしていますか？",
      Words: ["表記", "どう", "しています"],
      Lemmas: ["表記", "どう", "する"],
      Readings: ["ヒョウキ", "ドウ", "シテイマス"],
    },
    {
      Sentence:
        "　 ⇒「vs.」は本来小文字で「省略符（ピリオド）」が必要ですが、「大文字(前後の文字と同じ大きさということ)でも可」としていますか。",
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
      Sentence: "「省略符は不要ですか必要ですか」。",
      Words: ["省略", "符", "不要", "です", "必要", "です"],
      Lemmas: ["省略", "符", "不要", "です", "必要", "です"],
      Readings: ["ショウリャク", "フ", "フヨウ", "デス", "ヒツヨウ", "デス"],
    },
    {
      Sentence: "＜Ｃ＞『読み』はどうしていますか？",
      Words: ["読み", "どう", "しています"],
      Lemmas: ["読み", "どう", "する"],
      Readings: ["ヨミ", "ドウ", "シテイマス"],
    },
    {
      Sentence:
        "　 ⇒ 英語の発音はバーサス(versus 　ヴァーサス)ですが、この読み方は聞いたことがありません。",
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
      Sentence: 'ふつうは「○○"対"××」と読むでしょう。',
      Words: ["ふつう", "対", "読む", "でしょ"],
      Lemmas: ["ふつう", "対", "読む", "です"],
      Readings: ["フツウ", "タイ", "ヨム", "デショ"],
    },
    {
      Sentence: "ブイエス(ヴイエス)と読むこともありますか。",
      Words: ["読む", "こと", "あります"],
      Lemmas: ["読む", "こと", "ある"],
      Readings: ["ヨム", "コト", "アリマス"],
    },
    {
      Sentence:
        "局のアナウンサーだけでなく、外部のリポーターやナレーターにどのように読ませているでしょうか。",
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
      Sentence: "テレビ朝日の報道では、表記も読みもルールはない。",
      Words: ["テレビ朝日", "報道", "表記", "読み", "ルール"],
      Lemmas: ["テレビ朝日", "報道", "表記", "読む", "ルール"],
      Readings: ["テレビアサヒ", "ホウドウ", "ヒョウキ", "ヨミ", "ルール"],
    },
    {
      Sentence:
        "ただ、最近よく出て来るものの、そもそも「vs.」は「日本語ではない」（外来語でもない）と思うのだが・・・・。",
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
    },
  });

  onMount(() => {
    docs.forEach((doc, i) => index.add({ id: i, ...doc }));
  });

  async function fetchSentences() {
    const result = index.search(searchValue, { enrich: true }) as any[];
    const b = new Set(result.flatMap((a) => a.result));
    const a = Array.from(b.values());
    const docSentences = a.map((i) => docs[i].Sentence);
    sentences = docSentences.map((s, i) => ({
      id: i,
      sentence: s,
      tags: ["A", "B"],
      language: "JA",
      translations: [],
    }));

    console.log(JSON.stringify(a));
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
