from manim import *
import numpy as np
import random

config.background_color = WHITE
dark_red = "#9A0000"
light_red = "#9A000045"
dark_pink = "#9C1568"
light_pink = "#9C15686F"
dark_blue = "#336699"
medium_blue = "#7597BE"
light_blue = "#33669962"
dark_green = "#5E913B"
light_green = "#5D913B66"
dark_orange = "#E66914"
light_orange = "#E668149B"
dark_purple = "#5802A6"
light_purple = "#5702A68C"
dark_terquise = "#02A6A1"
dark_not_green = "#46A602"
axes_background_color = "#D3D3D3"
topics_backGround_color = "#0D113EFF"

class TitleScene(Scene):

    def show_warning(self, body: MathTex,set_image=False,return_not_show=False):
        """Show warning message with box"""

        title_text = Text("❗Note❗", color=dark_red, font_size=36)

        group = VGroup(title_text, body).arrange(DOWN, buff=0.3)

        box = RoundedRectangle(
            corner_radius=0.3,
            color=dark_red,
            fill_color=light_red,
            fill_opacity=0.2,
            width=group.width+0.5,
            height=group.height+0.5
        )

        box.move_to(group.get_center())

        if set_image==True:
            # ex_mark_1 = ImageMobject("images/ex_mark_1_img.png").move_to(box.get_top()+ 3*LEFT + 1.5*UP ).scale(3)
            # self.add(ex_mark_1) 

            ex_mark_2 = ImageMobject("images/ex_mark_2_img.png").move_to(box.get_top()+ 1.5*UP ).scale(3)
            self.add(ex_mark_2)

            # arrow_0_0_down = CurvedArrow(
            #     start_point=box.get_corner(UR)+2*UP+1.5*LEFT,
            #     end_point=box.get_top()+1.0*RIGHT,
            #     angle=PI/2,
            #     color=light_red,
            # ).scale(1.5)
            # self.play(
            #     Create(arrow_0_0_down),
            #     run_time=1
            # )
        if return_not_show==False:
            self.play(Create(box), Write(group))
            self.wait(2)
            self.play(FadeOut(group), FadeOut(box))

        if set_image==True:
            self.play(
                # FadeOut(arrow_0_0_down),
                # FadeOut(ex_mark_1),
                FadeOut(ex_mark_2)
            )
        if return_not_show==True:
            return group, box
        
    def show_minorPoint(self,body,return_notShow):
        """Show message with box to ask a question. """

        title_text = Text("Note", color=dark_blue, font_size=36)

        group = VGroup(title_text, body).arrange(DOWN, buff=0.3)

        box = RoundedRectangle(
            corner_radius=0.3,
            color=dark_blue,
            fill_color=light_blue,
            fill_opacity=0.2,
            width=group.width + 0.5,
            height=group.height + 0.5
        )
        

        box.move_to(group.get_center())

        if return_notShow :
            return group, box

        self.play(Create(box), Write(group))
        self.wait(2)
        self.play(FadeOut(group), FadeOut(box))
        return group, box

    def construct(self):

        # self.scene1()

        self.scene2()

        # self.scene3()

    def scene3(self,):
        pic = ImageMobject("images/end_pic.png").scale(2)
        self.play(
            FadeIn(pic),
        )
        continue_text = Text(
            "The end .",color=BLACK,font_size=80,
        ).shift(1*DOWN)
        self.play(
            Write(continue_text),
        )
        self.wait(1)

    def scene1(self):

        plane = NumberPlane(
            y_range=[-6, 10, 1],
            x_range=[-10, 10, 1],
            background_line_style={
                "stroke_color": GRAY,
                "stroke_opacity": 0.5
            },
            y_length=10,
            x_length=15,
        ).move_to(DOWN)
        self.play(Create(plane))

        title = Tex(
            "Banach Spaces",
            color=BLACK, font_size=80
        ).to_edge(UP)

        circle_metric = Circle(4,dark_pink,fill_color=dark_pink,fill_opacity=0.1)
        text_metric_space = MathTex(r"\text{Metric space}",color=dark_pink).scale(2).move_to(circle_metric.get_center()+2.3*UP)

        circle_norm = Circle(2.8,dark_purple,fill_color=dark_purple,fill_opacity=0.1).shift(1*DOWN)
        text_norm_space = MathTex(r"\text{Normed space}",color=dark_purple).scale(1.5).move_to(circle_norm.get_center()+1.3*UP)

        circle_banach = Circle(1.8,dark_orange,fill_color=dark_orange,fill_opacity=0.1).shift(1.8*DOWN)
        text_banach_space = MathTex(r"\text{Banach space}",color=dark_orange).scale(1.2).move_to(circle_banach.get_center()+0.2*UP)

        all_shapes = VGroup(*[
            circle_metric,
            text_metric_space,
            circle_norm,
            text_norm_space,
            circle_banach,
            text_banach_space
        ]).scale(0.7).to_corner(DR)

        self.play(
            FadeIn(title),
        )
        self.play(
            FadeIn(all_shapes),
        )

        function_space = MathTex(r"\text{Function space}",color=dark_pink).scale(2).move_to(title.get_center()+3*LEFT+1*DOWN)
        vectors_text = MathTex(r"\text{vectors}",r"\to",r"\text{functions}",color=BLACK).scale(1.5).next_to(function_space,DOWN)
        # functions_text = MathTex(,color=BLACK).next_to(function_space,DOWN)
        addition_text = MathTex(r"(f+g)(x) ",r"= f(x) + g(x)",color=BLACK).scale(1.5).next_to(vectors_text,DOWN)
        multiply_text = MathTex(r"(\lambda \, f)(x) ",r"= \lambda \, f(x)",color=BLACK).scale(1.5).next_to(addition_text,DOWN)

        self.play(
            TransformFromCopy(text_metric_space, function_space),
        )
        self.play(
            Write(vectors_text),
        )
        self.play(
            Write(addition_text),
        )
        self.play(
            Write(multiply_text),
        )

        self.wait(1)

        
        title_example1 = Tex(
            "Example 1",
            color=dark_green, font_size=80
        ).to_edge(UP)

        space_c_1_1 = MathTex(r"\text{Space } C( [-1, 1] )",color=dark_pink).scale(1.5).move_to(title.get_center()+3*LEFT+1*DOWN)
        definition_text = MathTex(r"g,",r"f : [-1, 1] \to \mathbb{R}",color=BLACK).scale(1.3).next_to(space_c_1_1,DOWN)
        continues1_text = MathTex(r"Continuous",color=dark_blue).move_to(addition_text[1].get_center())
        continues2_text = MathTex(r"Continuous",color=dark_blue).move_to(multiply_text[1].get_center())

        self.play(
            FadeTransform(title, title_example1),
        )
        self.play(
            FadeTransform(function_space, space_c_1_1),
        )
        self.wait(0.5)
        self.play(
            FadeTransform(vectors_text, definition_text),
        )
        self.wait(0.5)
        self.play(
            FadeTransform(addition_text[1], continues1_text),
            FadeTransform(multiply_text[1], continues2_text),
        )

        self.wait(1)

        self.play(
            FadeOut(VGroup(*[definition_text[0], addition_text[0], continues1_text, multiply_text[0], continues2_text])),
            definition_text[1].animate.shift(0.2*LEFT),
        )

        norm_example1 = MathTex(r"\|f\| = \int_{-1}^{1} |f(x)| \, dx",color=dark_purple).scale(1.2).next_to(definition_text[1],DOWN)

        self.play(
            TransformFromCopy(text_norm_space, norm_example1),
        )
        self.wait(1)

        banach_space = MathTex(r"\text{Banach space}",color=dark_orange).scale(1.2).next_to(norm_example1,DOWN,buff=0.5)
        image_cross = ImageMobject("images/red_cross.png").scale(1.2).move_to(banach_space.get_center())

        self.play(
            TransformFromCopy(text_banach_space, banach_space),
        )
        self.wait(0.5)
        self.add(image_cross)
        self.wait(1)

        self.play(
            FadeOut(all_shapes),
        )

        encounterexample = MathTex(
            r"f_n(x) = \begin{cases} "
            r"-1 & \text{if } x \in [-1, -\frac{1}{n}], \\ "
            r"nx & \text{if } x \in [-\frac{1}{n}, \frac{1}{n}] \\ "
            r"1 & \text{if } x \in [\frac{1}{n}, 1]. "
            r"\end{cases}",
            color=dark_blue,
        ).scale(1.2).move_to(title_example1.get_center()+2*DOWN+2.7*RIGHT)

        self.play(
            VGroup(*[space_c_1_1, definition_text[1], norm_example1, banach_space]).animate.shift(1.3*LEFT),
            image_cross.animate.shift(1.3*LEFT),
            FadeIn(encounterexample),
        )
        self.wait(0.5)

        cauchy_sequence_dis = MathTex(r"\|f_i - f_j\| = \left| \, \frac{1}{i} - \frac{1}{j} \, \right|",r"\to 0",color=dark_blue).next_to(encounterexample,DOWN)
        cauchy_sequence = MathTex(r"\text{Cauchy sequence}",color=dark_blue).scale(1.2).move_to(cauchy_sequence_dis.get_center())
        
        self.play(
            TransformFromCopy(VGroup(*[norm_example1, encounterexample]), cauchy_sequence_dis[0]),
        )
        self.wait(0.5)
        self.play(
            Write(cauchy_sequence_dis[1])
        )
        self.play(
            FadeTransform(cauchy_sequence_dis, cauchy_sequence),
        )
        self.wait(0.5)
        convergant_sequence = MathTex(r"\text{NOT}", r"\text{ a convergent sequence}",color=dark_blue).scale(1.2).move_to(cauchy_sequence_dis.get_center()+DOWN)
        convergant_sequence.set_color_by_tex(r"\text{NOT}",dark_red)
        converge_to = MathTex(
            r"f_n(x) \to f(x) = ",
            r"\begin{cases} -1 & x < 0 \\ 0 & x = 0 \\ 1 & x > 0 \end{cases}",
            # r"\notin C([-1, 1])",
            color=BLACK,
        ).move_to(cauchy_sequence_dis.get_center()+1.5*DOWN)
        continues3_text = MathTex(r"\text{NOT }",r"\text{Continuous}",color=dark_blue).shift(converge_to.get_center() + 0.7*DOWN + 1.5*LEFT)
        continues3_text.set_color_by_tex(r"\text{NOT }",dark_red)
        not_in_text = MathTex(r"f_n(x) \to f(x) \notin C([-1,1])",color=dark_blue).move_to(cauchy_sequence_dis.get_center()+DOWN)
        self.play(
            Write(converge_to),
        )
        self.wait(0.5)
        self.play(
            Write(continues3_text),
        )
        self.wait(0.5)
        self.play(
            FadeTransform(VGroup(*[continues3_text, converge_to]), not_in_text),
        )
        self.wait(0.5)
        self.play(
            TransformMatchingShapes(VGroup(*[not_in_text]), convergant_sequence),
        )
        self.wait(0.5)

        note = MathTex(r"\text{Sequences of continuous functions can } \\ \text{converge to discontinuous functions.}",color=BLACK).scale(0.8)
        text,box = self.show_warning(note,False,True)
        text.move_to(encounterexample.get_center()+0.5*DOWN)
        box.move_to(text.get_center())
        self.play(
            TransformMatchingShapes(VGroup(*[encounterexample, cauchy_sequence, convergant_sequence]), box),
            Write(text),
        )
        self.wait(0.5)

        fade_out_list = [
            text,
            box,
            space_c_1_1,
            definition_text[1],
            norm_example1,
            banach_space,
        ]
        title_example2 = Tex(
            "Example 2",
            color=dark_green, font_size=80
        ).to_edge(UP)
        self.play(
            FadeTransform(title_example1, title_example2),
            FadeOut(VGroup(*fade_out_list)),
            FadeOut(image_cross),
        )

        self.wait(1)

    def scene2(self):
        title_example2 = Tex(
            "Example 2",
            color=dark_green, font_size=80
        ).to_edge(UP)
        self.add(title_example2)
        plane = NumberPlane(
            y_range=[-6, 10, 1],
            x_range=[-10, 10, 1],
            background_line_style={
                "stroke_color": GRAY,
                "stroke_opacity": 0.5
            },
            y_length=10,
            x_length=15,
        ).move_to(DOWN)
        self.add(plane)

        circle_metric = Circle(4,dark_pink,fill_color=dark_pink,fill_opacity=0.1)
        text_metric_space = MathTex(r"\text{Metric space}",color=dark_pink).scale(2).move_to(circle_metric.get_center()+2.3*UP)

        circle_norm = Circle(2.8,dark_purple,fill_color=dark_purple,fill_opacity=0.1).shift(1*DOWN)
        text_norm_space = MathTex(r"\text{Normed space}",color=dark_purple).scale(1.5).move_to(circle_norm.get_center()+1.3*UP)

        circle_banach = Circle(1.8,dark_orange,fill_color=dark_orange,fill_opacity=0.1).shift(1.8*DOWN)
        text_banach_space = MathTex(r"\text{Banach space}",color=dark_orange).scale(1.2).move_to(circle_banach.get_center()+0.2*UP)

        all_shapes = VGroup(*[
            circle_metric,
            text_metric_space,
            circle_norm,
            text_norm_space,
            circle_banach,
            text_banach_space
        ]).scale(0.7).to_corner(DR)

        self.play(
            FadeIn(all_shapes),
        )

        space_definition_part1 = MathTex(
            r"\text{Space }",
            r"C ( [-1,1] )",
            color=dark_pink,
        ).scale(2)
        
        space_definition_part3 = MathTex(
            r" + ",
            color=dark_pink,
        ).scale(2)
        space_definition_part21 = MathTex(
            r"\|f\|_{\infty} = \sup_{x \in [-1,1]} |f(x)|",
            color=dark_pink,
        ).scale(1.5).move_to(space_definition_part3.get_center()+0.3*DOWN)
        space_definition_part22 = MathTex(
            r"\text{Banach space} \quad",r"\Large \checkmark",
            color=dark_pink,
        ).scale(1.5).move_to(space_definition_part21.get_center()+1*DOWN)
        space_definition_part22.set_color_by_tex(r"\Large \checkmark", GREEN)
        space_definition_part4 = MathTex(
            r"\text{The limit of every sequence} \\ \text{of continuous functions   }",
            color=dark_pink,
        ).scale(1.25)

        space_group = VGroup(space_definition_part1, #space_definition_part2,
                             space_definition_part3, space_definition_part4).arrange(DOWN,buff=0.4)
        space_group.next_to(all_shapes,LEFT,buff=0.5).shift(UP+0.1*RIGHT)

        l1space = MathTex(
            # r"L^1 - space",
            r"L^1([-1,1])",
            color=dark_pink,
        ).scale(1.5).move_to(title_example2.get_center()+3*LEFT+1*DOWN)

        space1 = VGroup(space_definition_part1,space_definition_part21,space_definition_part22).arrange(DOWN,buff=0.5).shift(2.5*LEFT)

        self.play(
            TransformFromCopy(text_metric_space, space1),
        )
        self.wait(2)
        self.play(
            TransformMatchingTex(space1, space_group),
        )
        self.wait(2)
        self.play(
            TransformMatchingShapes(space_group, l1space)
        )

        note_l1space_part1 = MathTex(
            r"\text{In } L^1 \text{space two functions}",
            color=BLACK,
        ).scale(1.2)
        note_l1space_part2 = MathTex(
            r"\text{are considered the same if} ",
            color=BLACK,
        ).scale(1.2)
        note_l1space_part3 = MathTex(
            r"\text{they are equal }",
            r"\text{almost}",
            color=BLACK,
        ).scale(1.2)
        note_l1space_part3.set_color_by_tex(r"\text{almost}",dark_red)
        note_l1space_part4 = MathTex(
            r"\text{everywhere.}",
            color=BLACK,
        ).scale(1.2)
        final_note = Text("Only for a countable set of \npoints can two functions \n  have different values.",color=BLACK,font_size=30)
        note_l1space = VGroup(*[note_l1space_part1, note_l1space_part2, note_l1space_part3, note_l1space_part4]).arrange(DOWN,buff=0.2)
        text, box = self.show_minorPoint(note_l1space, True)
        text.next_to(l1space,DOWN,buff=0.3)
        box.move_to(text.get_center())
        VGroup(*[text,box]).scale(0.9)
        final_note.scale(1.2).next_to(box,DOWN,buff=0.3)
        self.play(
            Create(box),
            Write(text),
        )
        self.play(
            Write(final_note),
        )
        self.wait(2)
        self.play(
            FadeOut(VGroup(*[text,box, final_note])),
        )
        self.wait(1.5)

        norm_example1 = MathTex(r"\|f\| = \int_{-1}^{1} |f(x)| \, dx",color=dark_purple).scale(1.2).next_to(l1space,DOWN)

        self.play(
            TransformFromCopy(text_norm_space, norm_example1),
        )
        self.wait(1)

        banach_space = MathTex(r"\text{Banach space} \quad",r"\Large \checkmark",color=dark_orange).scale(1.2).next_to(norm_example1,DOWN,buff=0.5)
        banach_space.set_color_by_tex(r"\Large \checkmark", GREEN)
        image_check = ImageMobject("images/tik .png").scale(0.1).next_to(banach_space,RIGHT).shift(0.2*UP)
        self.play(
            TransformFromCopy(text_banach_space, banach_space),
        )
        self.wait(0.5)
        # self.add(image_check)
        self.wait(1)

        fade_out_list = [
            all_shapes,
            l1space,
            norm_example1,
            banach_space,
            title_example2,
        ]
        self.play(
            FadeOut(VGroup(*fade_out_list)),
            # FadeOut(image_check),
        )
        self.play(
            FadeOut(plane),
        )

        self.wait(1)
