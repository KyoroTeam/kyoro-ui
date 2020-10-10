import '../../css/utils.css';

import { storiesOf } from '@storybook/svelte';
import { action } from '@storybook/addon-actions';
import ButtonSimple from '../../components/buttons/ButtonSimple.svelte';
import App from "../../../src/App.svelte";

storiesOf('Carbon | Carbon', module)
    //Simple Button
    .add(
        'Simple',
        () => ({
            Component: App,
            on: {
                customEventHandler: action('This custom event handler works'),
            },
        }),
    )
