<script setup>
import VueLogo from "./icons/VueLogo.vue"
import GithubLogo from "./icons/GithubLogo.vue"
const p = defineProps(["isLoading", "isEdited", "postAction", "result", "renderHtml"])
async function btnCopy() {
    await navigator.clipboard.writeText(p.result);
}
</script>

<template>
    <header>
        <nav class="container">
            <ul>
                <li>
                    <button v-if="isLoading" aria-busy="true">
                        AyaMark
                    </button>
                    <button v-else class="outline" @click="postAction">
                        <VueLogo /> AyaMark
                    </button>
                </li>
                <li>
                    <input type="checkbox" role="switch" @click="renderHtml" :checked="!isEdited">Render
                </li>
                <li v-show="result">
                    <a data-tooltip="点击复制" data-placement="bottom" @click="btnCopy">{{ result }}</a>
                </li>
            </ul>
            <ul>
                <li>
                    <a href="https://github.com/Brx86/AyaMark" target="_blank">
                        <GithubLogo />
                    </a>
                </li>
            </ul>
        </nav>
    </header>
</template>

<style scoped>
header {
    position: fixed;
    width: 100%;
    top: 0;
    background-color: white;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
}
</style>