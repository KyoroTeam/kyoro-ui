<script lang="ts">
  export let kanji: string;
  export let explination: string;
  import '../utils.css';
</script>

<div class="shadow-sm flex">
  <div class="text-red-600">{kanji}</div>
  <div>{explination}</div>
</div>
