<script setup>
import { ref, watchPostEffect } from "vue"
import { marked } from "marked"
import hljs from "highlight.js"
import NavBar from "./components/NavBar.vue"
marked.setOptions({ highlight: code => hljs.highlightAuto(code).value });


// const base_api = `${window.location.href}api`,
const base_api = `${window.location.href}api`,
  textLines = ref(5),
  textInput = ref(""),
  rHtml = ref(""),
  btnStatus = ref("outline"),
  isLoading = ref(false)

function renderHtml() {
  if (btnStatus.value) {
    rHtml.value = marked.parse(textInput.value)
    btnStatus.value = ""
  } else {
    btnStatus.value = "outline"
  }
}
async function postMarkdown() {
  isLoading.value = true

  const form = new FormData();
  form.append('c', "Hello World");

  const response = await fetch('http://localhost:7777/f', {
    method: 'POST',
    body: form
  })
  const r = await response.json()
  console.log(r)

  // const api_url = `${base_api}?p=${pkg_name.value}&m=${mirror.value}`
  // const response = await fetch(api_url)
  // const r = await response.json()
  isLoading.value = false
  // result.value = r.data
}
watchPostEffect(() => { textLines.value = Math.max(textInput.value.split("\n").length + 3), 5 })
</script>

<template>
  <NavBar :is-loading="isLoading" :post-action="postMarkdown" :btn-status="btnStatus" :render-html="renderHtml" />
  <main class="container">
    <article>
      <textarea v-if="btnStatus" v-model="textInput" :rows="textLines" placeholder="Type Markdown here..."></textarea>
      <div v-else v-html="rHtml"></div>
    </article>
  </main>
</template>

<style scoped>
article {
  min-height: 200px
}

article div {
  margin-top: 60px;
}

textarea {
  margin-top: 50px;
  margin-bottom: 0px;
  border: none;
  outline: none;
  resize: none;
}
</style>