<script lang="ts">
  import { Search, ButtonSet } from "carbon-components-svelte";
  import type { JibikiSenteceResponse, SentecePart } from "src/models/Jibiki";
  import SentenceSourceSelect from "../SentenceSourceSelect.svelte";
  import { Document } from "flexsearch";
  import { onMount } from "svelte";
  // import { getLocalContentList } from "src/services/anki";
  import { OfflineIndex } from "../../stores/offlineIndexStore";

  export let sentences: JibikiSenteceResponse[];

  let searchValue = "";

  onMount(() => {
    // Docs.forEach((doc, i) => index.add({ id: i, ...doc }));
    // getLocalContentList().then((content) => console.log(content));
  });

  function getHighloteSentenceParts(
    s: Solr.KyoTokenResult,
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

  $: {
    const result = OfflineIndex.search(searchValue, {
      enrich: true,
    }) as FlexSearch.RootObject[];

    console.log(searchValue, JSON.stringify(result));

    const b = new Set(result.flatMap((a) => a.result.map((r) => r.doc)));
    const a = Array.from(b.values());

    sentences = a.map((s, i) => ({
      id: i,
      sentence: s.Sentence,
      sentenceParts: getHighloteSentenceParts(s, searchValue),
      tags: ["A", "B"],
      language: "JA",
      translations: [],
    }));
  }
</script>

<ButtonSet style={"width:100%"}>
  <Search bind:value={searchValue} placeholder="Enter a phrase..." />
  <SentenceSourceSelect />
</ButtonSet>
