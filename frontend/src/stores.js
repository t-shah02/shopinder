import { writable } from 'svelte/store';


export const isUserLoggedIn = writable(false);
export const name = writable("");
export const shoppingList = writable([]);
export const email = writable("");
export const phoneNumber = writable("");
