import '../../css/utils.css';

import { storiesOf } from '@storybook/svelte';
import { action } from '@storybook/addon-actions';
import ButtonSimple from '../../components/buttons/ButtonSimple.svelte';
import Header from "../../../src/components/Header.svelte"

storiesOf('Buttons | Buttons', module)
    //Simple Button
    .add(
        'Simple',
        () => ({
            Component: Header,
            on: {
                customEventHandler: action('This custom event handler works'),
            },
        }),
    )
