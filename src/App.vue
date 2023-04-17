<script setup>
import { onBeforeMount, ref, watchPostEffect } from "vue"
import { marked } from "marked"
import hljs from "highlight.js"
import NavBar from "./components/NavBar.vue"
import DiaLog from "./components/DiaLog.vue"
marked.setOptions({ highlight: code => hljs.highlightAuto(code).value });
onBeforeMount(() => { result.value = { message: "", short: "" } })

const base_api = `${window.location.href}api`,
  textLines = ref(5),
  textInput = ref(""),
  rHtml = ref(""),
  isEdited = ref(true),
  isLoading = ref(false),
  result = ref(null)

function renderHtml() {
  if (isEdited.value) {
    isEdited.value = false
    rHtml.value = marked.parse(textInput.value)
  } else {
    isEdited.value = true
  }
}
async function postAction() {
  isLoading.value = true
  const form = new FormData();
  const blob = new Blob([textInput.value], { type: "text/txt" });
  form.append('c', blob);
  const response = await fetch('http://localhost:7777/f', { method: 'POST', body: form })
  result.value = await response.json()
  isLoading.value = false
}
watchPostEffect(() => { textLines.value = Math.max(textInput.value.split("\n").length + 3), 5 })
</script>

<template>
  <NavBar :is-loading="isLoading" :post-action="postAction" :render-html="renderHtml" />
  <main class="container">
    <article>
      <textarea v-if="isEdited" v-model="textInput" :rows="textLines" placeholder="Type Markdown here..."></textarea>
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