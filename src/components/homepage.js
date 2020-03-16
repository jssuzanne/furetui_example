import { defineComponent } from 'furetui/src/components/factory';

console.log('plop')

defineComponent('homepage', {
  template: `
    <div class="container has-text-centered content">
      <h1 class="title">Welcome in my own Furet UI</h1>
      <div class="column is-half is-offset-one-quarter">
        <img class="image" v-bind:src="logo" alt="Logo">
      </div>
      <p>
        This is just an example of AnyBlok / FuretUI
      </p>
    </div>
  `,
});
