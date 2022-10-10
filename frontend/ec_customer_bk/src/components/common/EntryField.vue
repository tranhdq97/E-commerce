<template>
    <div>
        <div class="title">{{ title }}</div>
        <input class="entry-field" :placeholder="placeHolder" :type="inputType" />
        <div class="error">{{ error }}</div>

    </div>

</template>

<script>
export default ({
    props: {
        title: '',
        placeHolder: '',
        inputType: "text",
        error: '',
    },
    // setup(props){
    //     console.log(props.title, props.placeHolder, props.inputType, props.error);
    // }
})
</script>