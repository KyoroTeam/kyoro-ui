<script lang="ts">
    import { Button } from "carbon-components-svelte";
    import Add16 from "carbon-icons-svelte/lib/Add16";
    import type { SelectTableRow } from "src/models/SelectTableRow";
    import type { ICardMapping } from "../stores/settingsStore";
    import { getContext } from "svelte";
    import type { IAnkiConnect } from "../services/ankiconect";
    const anki = getContext<IAnkiConnect>("anki");

    export let tableRows: SelectTableRow[] = [];
    export let targetMapping: ICardMapping;

    function onClicked() {}
</script>

<Button icon={Add16} disabled={tableRows.filter((r) => r.selected).length == 0}>
    Add Selected
    {targetMapping?.mappingName ?? 'Wow'}
</Button>
