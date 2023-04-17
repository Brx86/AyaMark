<script setup>
import { onBeforeMount, ref, watchPostEffect } from "vue"
import { marked } from "marked"
import hljs from "highlight.js"
import NavBar from "./components/NavBar.vue"
marked.setOptions({ highlight: code => hljs.highlightAuto(code).value });
const base_api = `//${window.location.hostname}:${window.location.port}`,
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
  const response = await fetch(`${base_api}/f`, { method: 'POST', body: form })
  result.value = `${base_api}/${(await response.json()).short}`
  isLoading.value = false
}
onBeforeMount(async () => {
  if (window.location.pathname !== "/") {
    isLoading.value = true
    const response = await fetch(`${base_api}/f${window.location.pathname}`)
    textInput.value = await response.text()
    rHtml.value = marked.parse(textInput.value)
    isEdited.value = false
    isLoading.value = false
  }
})
watchPostEffect(() => { textLines.value = Math.max(textInput.value.split("\n").length + 3), 5 })
</script>

<template>
  <NavBar :is-loading="isLoading" :is-edited="isEdited" :post-action="postAction" :result="result"
    :render-html="renderHtml" />
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