<script>
	import { createEventDispatcher, onDestroy } from 'svelte';
    import Icons from '../Icons/Icons.svelte';
	export let color = 'violet';
	export let avoidMaxHeight;
	const dispatch = createEventDispatcher();
	const close = () => dispatch('close');

	let modal;

	const handle_keydown = e => {
		if (e.key === 'Escape') {
			close();
			return;
		}

		if (e.key === 'Tab') {
			// trap focus
			const nodes = modal.querySelectorAll('*');
			const tabbable = Array.from(nodes).filter(n => n.tabIndex >= 0);

			let index = tabbable.indexOf(document.activeElement);
			if (index === -1 && e.shiftKey) index = 0;

			index += tabbable.length + (e.shiftKey ? -1 : 1);
			index %= tabbable.length;

			tabbable[index].focus();
			e.preventDefault();
		}
	};

	const previously_focused = typeof document !== 'undefined' && document.activeElement;

	if (previously_focused) {
		onDestroy(() => {
			previously_focused.focus();
		});
	}
</script>

<svelte:window on:keydown={handle_keydown}/>

<div class="fixed top-0 left-0 w-full h-full bg-neutral-200/25" on:click={close}></div>

<div class="z-20 modal {avoidMaxHeight?'':'height-control'} fixed top-1/4 left-1/2 overflow-auto bg-{color}-300 rounded max-w-lg -translate-x-1/2 -translate-y-1/4" role="dialog" aria-modal="true" bind:this={modal}>
    <div class="flex w-full justify-between p-4 border-b border-{color}-600">
        <slot name="title"></slot>
        <!-- svelte-ignore a11y-autofocus -->
        <button class="block" autofocus on:click={close}>
            <Icons name="close" tailwind="flex-no-shrink h-5 w-5 text-{color}-900 hover:stroke-2" />
        </button>
    </div>
	<slot></slot>
	<hr>
</div>

<style>
	.modal {
		width: calc(100vw - 4em);
	}
	.modal.height-control {
		height: calc(100vh - 4em);
	}
</style>