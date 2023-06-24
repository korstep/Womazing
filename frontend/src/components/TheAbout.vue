<template>
  <div class="about">
    <div class="container">
      <div class="about__body">
        <div class="about__history">
          <div class="about__image">
            <img src="@/assets/media/images/about1.png" alt="" />
          </div>
          <div class="about__text">
            <h3 class="about__subtitle">Идея и женщина</h3>
            <div class="about__description">
              <p>
                Womazing была основана в 2010-ом и стала одной из самых успешных
                компаний нашей страны. Как и многие итальянские фирмы, Womazing
                остаётся семейной компанией, хотя ни один из членов семьи не
                является модельером.
              </p>
              <br />
              <p>
                Мы действуем по успешной формуле, прибегая к услугам известных
                модельеров для создания своих коллекций. Этот метод был описан
                критиком моды Колином Макдауэллом как форма дизайнерского
                со-творчества, характерная для ряда итальянских prêt-a-porter
                компаний.
              </p>
            </div>
          </div>
        </div>
        <div class="about__history">
          <div class="about__text">
            <h3 class="about__subtitle">Магия в деталях</h3>
            <div class="about__description">
              <p>
                Первый магазин Womazing был открыт в маленьком городке на севере
                страны в 2010-ом году. Первая коллекция состояла из двух пальто
                и костюма, которые были копиями парижских моделей.
              </p>
              <br />
              <p>
                Несмотря на то, что по образованию основательница была
                адвокатом, ее семья всегда была тесно связана с шитьём
                (прабабушка основательницы шила одежду для женщин, а мать
                основала профессиональную школу кроя и шитья). Стремление
                производить одежду для масс несло в себе большие перспективы,
                особенно в то время, когда высокая мода по-прежнему
                доминировала, а рынка качественного prêt-a-porter попросту не
                существовало.
              </p>
            </div>
          </div>
          <div class="about__image">
            <img src="@/assets/media/images/about2.png" alt="" />
          </div>
        </div>
        <a href="#" class="about__btn">Перейти в магазин</a>
      </div>
    </div>
  </div>
</template>
<script>
export default {}
</script>
<style lang="scss">
.about__body {
  padding-top: 50px;
  display: flex;
  flex-direction: column;
  row-gap: 100px;
}

.about__history {
  display: flex;
  justify-content: space-between;
}

.about__image {
  max-height: 550px;
  max-width: 440px;
}

.about__text {
  max-width: 540px;
  align-self: center;
  display: flex;
  flex-direction: column;
  row-gap: 45px;
}

.about__description {
  @include text;
}

.about__subtitle {
  @include heading-h3;
}

.about__btn {
  @include button-filled;
  align-self: center;
}
</style>
