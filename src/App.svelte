<script lang="ts">
    import Nav from './components/nav.svelte';
    import Button from './components/Button.svelte';
    let menuItems = [
        { link: '#', name: 'Docs' },
        { link: '#', name: 'Home' },
        { link: '#', name: 'Blog' },
    ];
    const a: string = 'string';
</script>

<Nav {menuItems} />
<Button text={a} />
