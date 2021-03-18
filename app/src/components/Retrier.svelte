<script lang="ts">
    import { onDestroy, onMount } from "svelte";

    export let retryTime: number = 5000;
    export let maxCounts: number = 5;
    export let onTimeoutEnded: () => Promise<any>;

    let interval: NodeJS.Timeout;
    let currentCount = 0;
    let loading: boolean = false;

    function tick() {
        ++currentCount;
        if (currentCount >= maxCounts) {
            currentCount = 0;
            loading = true;
            clearInterval(interval);
            onTimeoutEnded()
                .catch(() => {
                    interval = setInterval(tick, retryTime);
                })
                .finally(() => (loading = false));
        }
    }

    onMount(() => {
        interval = setInterval(tick, retryTime);
    });

    onDestroy(() => {
        clearInterval(interval);
    });
</script>

<slot timeUntilNextTry={maxCounts - currentCount} {loading} />
